from pathlib import Path
from maze_solver.graph.solver import solve
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer
from maze_solver.maze_creation import mazes_path
from maze_solver.graph.solve_print import solve_and_print


maze_file_path = mazes_path() / "miniature.maze"
maze = Maze.load(maze_file_path)


solution = solve(maze)
print("entrance: ", maze.entrance)
print("exit: ", maze.exit)
print([square.index for square in solution])


#SVGRenderer().render(maze).preview()