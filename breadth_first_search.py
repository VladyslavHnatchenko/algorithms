"""Graph Breath-First Search"""

from collections import deque
from queue import Queue
from binary_tree import BinaryTree

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.appendleft((next, path+[next]))


print(list(bfs_paths(graph, 'A', 'F')))
print("\n")


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


print(shortest_path(graph, 'A', 'F'), "\n")
print(shortest_path(graph, 'E', 'D'), "\n")
print(shortest_path(graph, 'A', 'D'), "\n")
print(shortest_path(graph, 'F', 'D'), "\n")

# ------------------------------------------------------------------- #
# def bfs(graph, start):
#     visited, queue = [], deque([start])
#     while queue:
#         vertex = queue.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             queue.extendleft(set(graph[vertex]) - set(visited))
#     return visited
#
#
# print(bfs(graph, 'A'))

# ------------------------------------------------------------------- #
# class BFS(BinaryTree):
#
#     def bfs(self):
#         queue = Queue()
#         queue.put(self)
#
#         while not queue.empty():
#             current_node = queue.get()
#             print(current_node.value)
#
#             if current_node.left_child:
#                 queue.put(current_node.left_child)
#
#             if current_node.right_child:
#                 queue.put(current_node.right_child)
