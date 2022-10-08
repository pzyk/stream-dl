"""
Utilities
"""


def parse_interval(interval: str):
    """
    Parses interval string and returns integer
    """
    if interval.endswith("h"):
        return int(interval.replace("h", "")) * 3600
    if interval.endswith("m"):
        return int(interval.replace("m", "")) * 60
    if interval.endswith("s"):
        return int(interval.replace("s", ""))

    return 0


def str_to_bool(value: str):
    """
    Converts string to bool
    """
    if value.strip().lower() == "false":
        return False
    if value.strip().lower() == "true":
        return True

    return None
