"""Class to Print Maze"""




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
                    case "|":
                        print_success("|", "")
                    case "-":
                        print_success("-", "")
                    case "u":
                        print_success("u", "")
                    case "r":
                        print_success("r", "")
                    case "d":
                        print_success("d", "")
                    case "l":
                        print_success("l", "")
            print()
        print()
