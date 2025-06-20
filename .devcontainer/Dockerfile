# ------------------------------------------------------------
#   Dockerfile  ―  CPU 専用（Apple Silicon / x86 共通）
#   *CUDA を使わない最軽量構成*
# ------------------------------------------------------------
FROM python:3.10.18-slim-bookworm             

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

# ------------------------------------------------------------
# ② OS ライブラリ（SoftSort ビルド & 画像描画用）
# ------------------------------------------------------------
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      git build-essential cmake pkg-config \
      libgl1-mesa-glx libglib2.0-0 wget \
 && apt-get upgrade -y \          
 && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# ③ 依存パッケージを二段階でインストール
#    ─ torch だけは後で CPU wheel 指定 ─
# ------------------------------------------------------------
COPY requirements.txt .
RUN pip install -U pip && \
    grep -vE '^torch' requirements.txt > req_notorch.txt && \
    pip install -r req_notorch.txt

# ---------- PyTorch / torchvision / torchaudio (CPU wheel)
RUN pip install --index-url https://download.pytorch.org/whl/cpu \
    torch==2.2.* torchvision torchaudio

# ---------- SoftSort（torchsort） ← SoftSort-Knapsack用
RUN pip install torchsort==0.1.9

# ------------------------------------------------------------
# ④ プロジェクトソースをコピー  (必要なら .dockerignore を配置)
# ------------------------------------------------------------
COPY . .

CMD ["bash"]     # devcontainer なら自動で /bin/bash が開く
