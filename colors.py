"""Console Color Helpers"""


# I modified this file from the original.  The methods take in an extra argument
# to allow better printing customization.

# David Barnes
# CIS 226
# 05-28-23

# System imports
import os

os.system(
    ""
)  # Required to get the terminal to ALWAYS show colors instead of raw escape codes.


# Decorator to convert Style class to a Singleton
def singleton(cls):
    """Singleton function"""
    return cls()


# Class of different Styles
@singleton
class Style:
    """Contains constants for colors"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[2J"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value


def print_success(message, my_end="\n"):
    """Print success message"""
    Style.GREEN  # pylint:disable=W0104
    print(message, end=my_end)
    Style.RESET  # pylint:disable=W0104


def print_warning(message, my_end="\n"):
    """Print warning message"""
    Style.YELLOW  # pylint:disable=W0104
    print(message, end=my_end)
    Style.RESET  # pylint:disable=W0104


def print_error(message, my_end="\n"):
    """Print error message"""
    Style.RED  # pylint:disable=W0104
    print(message, end=my_end)
    Style.RESET  # pylint:disable=W0104


def print_primary(message, my_end="\n"):
    """Print primary message"""
    Style.BLUE  # pylint:disable=W0104
    print(message, end=my_end)
    Style.RESET  # pylint:disable=W0104


def print_info(message, my_end="\n"):
    """Print info message"""
    Style.CYAN  # pylint:disable=W0104
    print(message, end=my_end)
    Style.RESET  # pylint:disable=W0104
