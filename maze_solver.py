"""maze solver module"""

# System Imports

# First Party Imports
from maze_printer import MazePrinter


class MazeSolver:
    """maze solver class"""

    my_printer = MazePrinter()

    def __init__(self):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may wan to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.

        # this attribute keeps track of whether the maze is solved or not
        self.solving: bool = True
        self.direction = "up"

        # this attribute saves the bottom row index and

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""
        print("made it to traversal")
        self.__maze_traversal(maze, x_start, y_start)

        # I must reset the bool here to reuse the maze_solver instance later
        self.solving = True

    def __maze_traversal(self, maze, current_x, current_y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""

        print(f"current: {current_x} {current_y}")
        print(maze[current_y][current_x])
        try:
            match maze[current_y][current_x]:

                # First Base Case.
                # If the character is a # then the solver is at a wall and must go back

                case "^":
                    maze[current_y][current_x] = "X"
                    # move up
                    if self.solving:
                        self.__maze_traversal(maze, current_x, current_y - 1)
                case "#":
                    print(self.direction)
                    match self.direction:
                        case "up":
                            self.direction = "right"
                        case "right":
                            self.direction = "down"
                        case "down":
                            self.direction = "left"
                        case "left":
                            self.direction = "up"
                    print(self.direction)
                    return
                # Movement
                case ".":
                    maze[current_y][current_x] = "X"
                    if self.solving:
                        self.my_printer.print_maze(maze)
                    # move up
                    if self.solving:
                        self.__maze_traversal(maze, current_x, current_y - 1)
                    # move right
                    if self.solving:
                        self.__maze_traversal(maze, current_x + 1, current_y)
                    # move down
                    if self.solving:
                        self.__maze_traversal(maze, current_x, current_y + 1)
                    # move left
                    if self.solving:
                        self.__maze_traversal(maze, current_x - 1, current_y)

            if self.solving:
                self.my_printer.print_maze(maze)

        except IndexError:
            print("Out of range.")
            self.solving = False
            pass
