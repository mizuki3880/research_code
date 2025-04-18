FROM python:3.10

WORKDIR /workspace

# システム系パッケージ
RUN apt-get update && apt-get install -y \
    git build-essential wget \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージ（PyTorch, Transformers, Jupyterなど）
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
