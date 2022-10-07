#!/usr/bin/env python3
"""
Live stream downloader
"""
import threading

from config import Config
from downloader import Downloader
from logger import Logger
from utils import motd

logger = Logger(log_level=0)


def main():
    """
    Main function
    """
    motd()

    service_threads = {}
    config = Config("config/config.yaml")
    dl = Downloader(logger=logger)

    for service in config.services:
        logger.log("[>] Spawning service thread for " + service, 1)
        thread = threading.Thread(
            target=dl.loop,
            args=(service, config.services[service]["config"], config.services[service]["channels"]),
        )
        service_threads[service] = thread
        thread.start()


if __name__ == "__main__":
    main()
