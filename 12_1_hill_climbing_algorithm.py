import numpy as np


def shortest_path(graph, src, dst):
    """Find the shortest path from src to dst in a
    given undirected graph, represented as a dictionary."""

    visited = set()
    queue = [[src, 0]]  # we can emulate a queue if we use a list and
    # commit to using only .append() and .pop(0)

    while len(queue) > 0:
        cur_node, dist = queue.pop(0)

        if cur_node == dst:
            return dist
        if cur_node in visited:
            continue

        visited.add(cur_node)
        for neighbour in graph[cur_node]:
            queue.append([neighbour, dist + 1])

    return -1  # if there is no path


def build_graph(matrix):
    """Creates an adjacency list from an edges list."""

    graph = {}
    matrix_height, matrix_width = matrix.shape

    for x in range(matrix_width):
        for y in range(matrix_height):
            graph[x, y] = []
            cur_height = matrix[y, x]
            for neighbour in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if (
                    neighbour[0] < 0
                    or neighbour[0] >= matrix_width
                    or neighbour[1] < 0
                    or neighbour[1] >= matrix_height
                ):
                    continue
                if matrix[neighbour[1], neighbour[0]] <= cur_height + 1:
                    graph[x, y].append(neighbour)

    return graph


with open("./data/input12.txt") as f:
    contents = f.read().splitlines()

ORD_A = ord("a")
ORD_S = ord("S") - ORD_A
ORD_E = ord("E") - ORD_A

heights_list = [[ord(height) - ORD_A for height in row] for row in contents]
heights = np.array(heights_list)

y_start, x_start = np.where(heights == ORD_S)
x_start, y_start = x_start[0], y_start[0]
y_end, x_end = np.where(heights == ORD_E)
x_end, y_end = x_end[0], y_end[0]

heights[y_start, x_start] = 0
heights[y_end, x_end] = ord("z") - ord("a")

graph = build_graph(heights)

print(shortest_path(graph, (x_start, y_start), (x_end, y_end)))
