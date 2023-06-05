FROM python:3.9-slim

ENV UID=99 \
    GID=100 \
    LOG_LEVEL=1 \
    YTDL_ARGS="quiet"

WORKDIR /app

COPY --chown=$UID:$GID . .

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install --no-install-recommends ffmpeg && \
    apt-get autoremove && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd -s /bin/bash -u $UID abc && \
    usermod -g $GID abc && \
    rm requirements.txt && \
    rm -rf /var/lib/apt/lists/* && \
    mv config /

USER abc

VOLUME /config /downloads

ENTRYPOINT python stream-dl.py -c /config/config.yaml -l $LOG_LEVEL -a $YTDL_ARGS