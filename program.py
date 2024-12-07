"""Program code"""

# Walter Podewil
# CIS 226
# 09/25/2024

# First-party imports
from maze_solver import MazeSolver
from maze_printer import MazePrinter


def main(*args):
    """Method to run program"""
    maze = read_maze("input_maze.txt")


def find_xs():
    """find count of Xs"""
    my_solver = MazeSolver()
    my_printer = MazePrinter()
    maze = read_maze("input_maze.txt")
    x_start, y_start = get_start_point(maze)
    my_solver.solve_maze(maze, x_start, y_start)
    my_printer.print_maze(maze)
    x_count = count_x(maze)
    print(x_count)

def read_maze(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    maze = []
    with open(filename, "r") as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


def get_start_point(maze):
    """find start coords"""
    for y_index, row_list in enumerate(maze):
        for x_index, char in enumerate(row_list):
            if char == "^":
                char = "."
                return (x_index, y_index)

def count_x(maze):
    """count number of xs in maze"""
    count = 0
    for y_index, row_list in enumerate(maze):
        for x_index, char in enumerate(row_list):
            if char == "X":
                count += 1
    return count
