"""Class to Print Maze"""

# Walter Podewil
# CIS 226
# September 23, 2024


# System Imports

# First Party Imports
from colors import (
    print_error,
    print_success,
    print_warning,
)

# Third Party Imports


class MazePrinter:
    """This class is used to print out the maze"""

    # my_x = "\uff38"
    # my_o = "\uff2f"

    def print_maze(self, maze: list):
        """Prints Maze with Color"""
        for row in maze:
            for column in row:
                match column:
                    case "#":
                        print("#", end="")
                    case ".":
                        print_warning(".", "")
                    case "X":
                        print_success("X", "")
                    case "O":
                        print_error("O", "")
            print()
        print()
