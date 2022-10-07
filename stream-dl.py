#!/usr/bin/env python3
"""
Live stream downloader
"""
import threading

from src.config import Config
from src.downloader import Downloader
from src.logger import Logger
from src.utils import motd

logger = Logger(log_level=0)


def main():
    """
    Main function
    """
    motd()

    service_threads = {}
    config = Config("config/config.yaml")
    dl = Downloader(logger=logger)

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
