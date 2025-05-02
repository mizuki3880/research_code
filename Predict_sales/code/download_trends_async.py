# download_trends_async.py
# ------------------------
# Playwright Async API で 269 日チャンクの Trends CSV を確実に DL（429対策・再試行機能付き）

import os
import datetime as dt
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# Jupyter 等で asyncio.run を使うためのパッチ
nest_asyncio.apply()

DOWNLOAD_DIR = "trends_csvs"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
MAX_RETRIES = 3        # 429 やタイムアウト時の再試行回数
RETRY_DELAY = 300      # 429 の場合に待機する秒数 (5分)
REQUEST_DELAY = 5      # 通常のチャンク間待機

async def download_trends():
    start = dt.date(2021, 6, 16)
    end   = dt.date(2025, 4, 28)
    span  = dt.timedelta(days=269)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(accept_downloads=True)
        page    = await context.new_page()

        s = start
        while s < end:
            e = min(s + span, end)
            period = f"{s}_{e}"
            url = (
                f"https://trends.google.com/trends/explore"
                f"?geo=JP&date={s:%Y-%m-%d}%20{e:%Y-%m-%d}"  
                "&q=%E5%8F%A4%E7%9D%80"
            )

            for attempt in range(1, MAX_RETRIES+1):
                try:
                    await page.goto(url)
                    await page.wait_for_load_state("networkidle")

                    content = await page.content()
                    if "429." in content:
                        print(f"[{period}] 429エラー検出: {attempt}/{MAX_RETRIES} リトライ前待機 {RETRY_DELAY}s")
                        await asyncio.sleep(RETRY_DELAY)
                        continue

                    # メニュー開き試行
                    try:
                        await page.click("button[aria-label='More options']", timeout=10000)
                        await asyncio.sleep(0.5)
                    except PlaywrightTimeout:
                        print(f"[{period}] メニュー非表示 or タイムアウト: フォールバック")

                    # ダウンロード試行
                    download = None
                    selectors = [
                        "button:has-text('Download CSV')",
                        "text=/Download CSV/i",
                        "text=/CSV をダウンロード/i",
                        "xpath=//a[@download]",
                        "css=a[download]"
                    ]
                    for sel in selectors:
                        try:
                            async with page.expect_download() as dl_info:
                                await page.click(sel, timeout=10000)
                            download = await dl_info.value
                            break
                        except Exception:
                            continue

                    if not download:
                        raise RuntimeError(f"[{period}] Download CSV ボタンが見つからず")

                    # 保存
                    dest = os.path.join(DOWNLOAD_DIR, f"trend_{period}.csv")
                    await download.save_as(dest)
                    print(f"[{period}] ダウンロード成功: {dest}")
                    break

                except Exception as err:
                    if attempt == MAX_RETRIES:
                        raise
                    print(f"[{period}] エラー: {err}、{attempt}/{MAX_RETRIES} リトライ")
                    await asyncio.sleep(RETRY_DELAY)

            # 次チャンクへ待機
            await asyncio.sleep(REQUEST_DELAY)
            s = e + dt.timedelta(days=1)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(download_trends())
