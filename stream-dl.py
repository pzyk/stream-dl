#!/usr/bin/env python3
"""
Live stream downloader
"""
import argparse
import sys
import threading

from src.config import Config
from src.downloader import Downloader
from src.logger import Logger


def get_options(args):
    """
    Parse command line arguments
    """
    if args is None:
        return None

    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-c", "--config", help="Path to config file")
    parser.add_argument(
        "-l", "--log-level", help="0 = Debug, 1 = Info (default), 2 = Quiet"
    )
    parser.add_argument(
        "-a", "--ytdl-args", help="Pass arguments to yt-dlp (e.g. verbose, quiet)"
    )
    options = parser.parse_args(args)

    return options


def main():
    """
    Main function
    """
    options = get_options(sys.argv[1:])

    config_path = options.config if options.config else "/config/config.yaml"
    config = Config(config_path)

    log_level = options.log_level if options.log_level else 0
    logger = Logger(log_level=log_level)

    dl_args = options.ytdl_args if options.ytdl_args else ""

    service_threads = {}
    dl = Downloader(logger=logger, dl_args=dl_args)

    for service in config.services.items():
        logger.log("[>] Spawning service thread for " + service[0], 1)
        thread = threading.Thread(
            target=dl.loop,
            args=(service[0], service[1]["config"], service[1]["channels"]),
        )
        service_threads[service[0]] = thread
        thread.start()


if __name__ == "__main__":
    main()
