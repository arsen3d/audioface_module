# FROM python:3.9-slim
FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    curl \
    && wget https://dist.ipfs.io/kubo/v0.32.1/kubo_v0.32.1_linux-amd64.tar.gz \
    && tar -xvzf kubo_v0.32.1_linux-amd64.tar.gz \
    && cd kubo \
    && bash install.sh \
    && rm -rf kubo_v0.32.1_linux-amd64.tar.gz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install uv
RUN uv pip install --no-cache-dir -r requirements.txt --system

COPY src/ .

# CMD ["python", "."]
# RUN ipfs init
COPY docker.sh .
COPY docker-dev.sh .
CMD ["sh", "-c", "./docker.sh"]