# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを `/app` に設定
WORKDIR /app

# `requirements.txt` をコンテナにコピー
COPY requirements.txt /app/requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir -r /app/requirements.txt

# コンテナ起動時のデフォルトコマンド
CMD ["python3"]
