# Stream-DL
[![Docker Image Size](https://img.shields.io/docker/image-size/pzyk/stream-dl/latest?style=flat&logo=docker)](https://hub.docker.com/r/pzyk/stream-dl)
[![Docker Pulls](https://img.shields.io/docker/pulls/pzyk/stream-dl?style=flat&logo=docker)](https://hub.docker.com/r/pzyk/stream-dl)
[![Docker Stars](https://img.shields.io/docker/stars/pzyk/stream-dl?style=flat&logo=docker)](https://hub.docker.com/r/pzyk/stream-dl)
[![GitHub Downloads](https://img.shields.io/github/downloads/:pzyk/:stream-dl/total?style=flat&logo=github)](https://github.com/pzyk/stream-dl)
[![GitHub Stars](https://img.shields.io/github/stars/:pzyk/:stream-dl?style=flat&logo=github)](https://github.com/pzyk/stream-dl)
<!--[![GitHub License](https://img.shields.io/github/license/:pzyk/:stream-dl?style=flat&logo=github)](https://github.com/pzyk/stream-dl)-->
<!--[![GitHub Pipeline Status](https://img.shields.io/github/checks-status/:pzyk/:stream-dl/:main?style=flat&logo=github)](https://github.com/pzyk/stream-dl)-->
<!--[![GitHub Issues](https://img.shields.io/github/issues/:pzyk/:stream-dl?style=flat&logo=github)](https://github.com/pzyk/stream-dl)-->

#### A yt-dlp wrapper for automated downloading of live streams

## Installation

### Linux
```
git clone https://github.com/pzyk/stream-dl.git

cd stream-dl

pip install -r requirements.txt

vim config/config.yaml

python3 stream-dl.py -c config/config.yaml
```

### Docker

#### Docker Run
```
docker run -v /docker/stream-dl/config:/config -v /docker/stream-dl/output:/output pzyk/stream-dl:latest
```

#### Docker Compose
```yaml
version: "3"

services:

  stream-dl:
    image: pzyk/stream-dl:latest
    container_name: stream-dl
    environment:
      - UID=99                    # Optional
      - GID=100                   # Optional
      - LOG_LEVEL=1               # Optional
      - YTDL_ARGS="quiet,verbose" # Optional
    volumes:
      - /docker/stream-dl/config:/config
      - /docker/stream-dl/output:/output
    restart: unless-stopped
```

#### Environment Variables
| Variable    | Example Value                                 | Description                    |
|:------------|:----------------------------------------------|:-------------------------------|
| `UID`       | `99`                                          | User ID for file permissions   |
| `GID`       | `100`                                         | Group ID for file permissions  |
| `LOG_LEVEL` | `1`                                           | 0 = Debug, 1 = Info, 2 = Quiet |
| `YTDL_ARGS` | `"quiet,verbose,username=user,password=pass"` | Arguments to pass to yt-dlp    |

#### Image Tags
| Tag                | Description                                    |
|:-------------------|:-----------------------------------------------|
| `latest`           | Latest stable version                          |
| `202210082143`     | Specific stable version (format: YYYYmmddHHMM) |
| `dev`              | Latest development version                     |
| `dev-202210082143` | Specific stable version (format: YYYYmmddHHMM) |

## Configuration
```yaml
example_service:
  url: https://example.com/
  path: output
  interval: 5m
  channels:
    channel_1:
      url: example
      path: Example
```
| Example           | Description                                                                                                                                                  |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `example_service` | Name of the streaming service (choose whatever you like)                                                                                                     |
| `url`             | URL of the streaming service                                                                                                                                 |
| `path`            | Default output path for downloaded videos                                                                                                                    |
| `interval`        | Interval to check if streams are online (e.g. 10s, 5m, 1h)                                                                                                   |
| `channels`        | Fixed block name (do not change!)                                                                                                                            |
| `channel_1`       | Name of a channel to download (choose whatever you like)                                                                                                     |
| `url`             | URL of the streaming channel (will be appended to the URL of the streaming service; final download URL in this example would be https://example.com/example) |
| `path`            | Output path of the channel (subdirectory inside default output path)                                                                                         |
