"""Program code"""



# System Imports
from func_timeout import func_timeout, FunctionTimedOut
import copy
import sys

# First-party imports
from maze_solver import MazeSolver
from maze_printer import MazePrinter
from errors import InfiniteLoopError


def main(*args):
    """Method to run program"""
    my_solver = MazeSolver()
    my_printer = MazePrinter()
    maze = read_maze("input_maze.txt")
    infinite_loop_count = 0

    x_start, y_start = get_start_point(maze)
    for y_index, row_list in enumerate(maze):
        for x_index, character in enumerate(row_list):
            new_maze = copy.deepcopy(maze)
            if character == ".":
                new_maze[y_index][x_index] = "#"
                # my_printer.print_maze(new_maze)
                try:
                    my_solver.solve_maze(new_maze, x_start, y_start)

                except InfiniteLoopError:
                    # my_printer.print_maze(new_maze)
                    infinite_loop_count += 1

            new_maze[y_index][x_index] = "."

    print(f"infinite_loop_count: {infinite_loop_count}")


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
