FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install ffmpeg && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd -s /bin/bash -u 99 abc && \
    usermod -g 100 abc && \
    rm -r .git && \
    rm -r .github && \
    rm config/config.yaml && \
    rm README.md && \
    rm Dockerfile && \
    rm requirements.txt

USER abc

ENTRYPOINT ["python", "stream-dl.py"]