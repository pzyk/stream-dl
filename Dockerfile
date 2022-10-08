FROM python:3.9

ENV UID=99 \
    GID=100 \
    LOG_LEVEL=1 \
    YTDL_ARGS="quiet,verbose"

WORKDIR /app

COPY --chown=99:100 . .

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install ffmpeg && \
    apt-get clean && \
    apt-get autoremove && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd -s /bin/bash -u 99 abc && \
    usermod -g 100 abc && \
    rm requirements.txt

USER abc

VOLUME /config /downloads

ENTRYPOINT ["python", "stream-dl.py -l $LOG_LEVEL -a $YTDL_ARGS"]