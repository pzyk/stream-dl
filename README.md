# Stream-DL
#### A yt-dlp wrapper for automated downloading of live streams
Docker Hub: https://hub.docker.com/r/pzyk/stream-dl

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
    image: pzyk/stream-dl
    container_name: stream-dl
    volumes:
      - /docker/stream-dl/config:/config
      - /docker/stream-dl/output:/output
    restart: unless-stopped
```

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
| Example         | Description                                                                                                                                                  |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| example_service | Name of the streaming service (choose whatever you like)                                                                                                     |
| url             | URL of the streaming service                                                                                                                                 |
| path            | Default output path for downloaded videos                                                                                                                    |
| interval        | Interval to check if streams are online (e.g. 10s, 5m, 1h)                                                                                                   |
| channels        | Fixed block name (do not change!)                                                                                                                            |
| channel_1       | Name of a channel to download (choose whatever you like)                                                                                                     |
| url             | URL of the streaming channel (will be appended to the URL of the streaming service; final download URL in this example would be https://example.com/example) |
| path            | Output path of the channel (subdirectory inside default output path)                                                                                         |
