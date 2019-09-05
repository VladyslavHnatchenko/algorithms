"""Graph Depth-First Search"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


print(list(dfs_paths(graph, 'A', 'F')))

# ------------------------------------------------------------------- #
# def iterative_dfs(graph, start, path=None):
#     """Iterative depth first search from start."""
#     if path is None:
#         path = []
#     q = [start]
#     while q:
#         v = q.pop()
#         if v not in path:
#             path = path + [v]
#             q += graph[v]
#     return path
#
#
# print(iterative_dfs(graph, 'A'))

# ------------------------------------------------------------------- #
# def dfs(graph, start):
#     visited, stack = [], [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             stack.extend(set(graph[vertex]) - set(visited))
#     return visited
#
#
# print(dfs(graph, 'A'))


# ------------------------------------------------------------------- #
# from binary_tree import BinaryTree
#
#
# class DFS(BinaryTree):
#
#     """pre-order, Depth-first search, DFS"""
#     def pre_order(self):
#         print(self.value)
#
#         if self.left_child:
#             self.left_child.pre_order()
#
#         if self.right_child:
#             self.right_child.pre_order()
#
#     """in-order, Depth-first search, DFS"""
#     def in_order(self):
#         if self.left_child:
#             self.left_child.in_order()
#
#         print(self.value)
#
#         if self.right_child:
#             self.right_child.in_order()
#
#     """post-order, Depth-first search, DFS"""
#     def post_order(self):
#         if self.left_child:
#             self.left_child.post_order()
#
#         if self.right_child:
#             self.right_child.post_order()
#
#         print(self.value)
