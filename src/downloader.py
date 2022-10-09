"""
Downloader
"""
import threading
import time

import yt_dlp

from src.utils import parse_interval, str_to_bool


class Downloader:
    """
    Class for downloader
    """

    def __init__(self, logger, dl_args: str):
        """
        Init
        """
        self.logger = logger
        self.dl_args = dl_args

    def loop(self, config: dict, channels: dict):
        """
        Loop which is started for each service
        Cycles through all channels and spawns threads to download them
        """
        threads = {}

        while True:
            for channel in channels:
                url = config["url"] + channels[channel]["url"]
                path = config["path"] + channels[channel]["path"]

                # Check if thread already exists
                if channel in threads:
                    thread = threads[channel]

                    if thread:
                        if thread.is_alive():
                            self.logger.log(
                                "[i] Download already running: " + url,
                                1,
                            )
                            continue

                        # Join thread if it exists but is stopped
                        self.logger.log("[i] Stopped thread found", 0)
                        thread.join()

                # Thread for channel does not exist
                self.logger.log("[>] Spawning thread for " + channel, 0)
                thread = threading.Thread(
                    target=self._download_channel, args=(url, path)
                )
                threads[channel] = thread
                thread.start()

            self.logger.log("[>] Sleeping for " + config["interval"], 0)
            interval = parse_interval(config["interval"])
            time.sleep(interval)

    def _download_channel(self, url: str, path: str):
        """
        Checks if channel is live
        Downloads stream
        """
        ytdl_options = {"paths": {"home": path}, "print-traffic": True}

        # Parse command line options
        for arg in self.dl_args.split(","):
            if arg:
                if "=" in arg:
                    value = (
                        arg.split("=")[1]
                        if arg.split("=")[1].lower() not in ("true", "false")
                        else str_to_bool(arg.split("=")[1])
                    )
                    ytdl_options[arg.split("=")[0]] = value
                else:
                    ytdl_options[arg] = True

        with yt_dlp.YoutubeDL(ytdl_options) as ytdl:
            try:
                self.logger.log("[>] Starting stream download: " + url, 1)
                ytdl.download([url])
                self.logger.log("[i] Stream downloaded successfully: " + url, 1)
            except yt_dlp.utils.DownloadError:
                # Don't crash if stream is offline
                self.logger.log("[!] Stream download failed: " + url, 1)
