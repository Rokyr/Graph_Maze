from maze_solver.graph.solver import solve


def solve_and_print(maze):
    solution = solve(maze)
    if solution:
        print("Solve Data:")
        print("Entrance:", maze.entrance)
        print("Exit:", maze.exit)
        print("Path:", solution.squares)
    else:
        print("No solution found.")