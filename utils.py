"""
Utilities
"""


def motd():
    """
    Print some neat ASCII art
    """
    message = (
        "##############################\n"
        "# Live Stream Downloader 0.1 #\n"
        "#          by pzyk           #\n"
        "##############################"
    )
    print(message)


def parse_interval(interval: str):
    """
    Parses interval string and returns integer
    """
    if interval.endswith("h"):
        return int(interval.replace("h", "")) * 3600
    elif interval.endswith("m"):
        return int(interval.replace("m", "")) * 60
    elif interval.endswith("s"):
        return int(interval.replace("s", ""))
