"""
Logger
"""


class Logger:
    """
    Class for logger
    """

    def __init__(self, log_level: int = 0):
        """
        Init method

        Log levels:
            0: Debug
            1: Info
            2: Quiet
        """
        self.log_level = int(log_level)

    def log(self, message: str, log_level: int):
        """
        Log message if log level allows it
        """
        if log_level >= self.log_level:
            print(message)
