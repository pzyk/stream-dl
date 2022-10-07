FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install ffmpeg && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd -s /bin/bash -u 99 abc && \
    usermod -g 100 abc && \
    rm config/config.yaml

USER abc

ENTRYPOINT ["python", "main.py"]