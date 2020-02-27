import logging
from typing import Callable

DEBUG = logging.debug
INFO = logging.info
WARNING = logging.warning
ERROR = logging.error
CRITICAL = logging.critical


def log_it(level: Callable, msg: str) -> None:
    root = logging.root
    root.setLevel = 0
    root.name = 'pybites_logger'
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")