from __future__ import annotations

import networkx as nx

from maze_solver.graph.converter import make_graph
from maze_solver.models.maze import Maze
from maze_solver.models.solution import Solution


def solve(maze: Maze) -> Solution | None:
    try:
        graph = make_graph(maze)
        print("Graph:", graph)
        print("Nodes:", graph.nodes)

        path = nx.shortest_path(graph, source=maze.entrance, target=maze.exit)
        print("Shortest Path:", path)

        return Solution(squares=tuple(path))
    except nx.NetworkXException:
        return None

# def solve(maze: Maze) -> Solution | None:
#     try:
#         return Solution(
#             squares=tuple(
#                 nx.shortest_path(
#                     make_graph(maze),
#                     source=maze.entrance,
#                     target=maze.exit,
#                 )
#             )
#         )
#     except nx.NetworkXException:
#         return None