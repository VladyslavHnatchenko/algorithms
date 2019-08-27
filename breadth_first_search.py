from queue import Queue

from binary_tree import BinaryTree


class BFS(BinaryTree):

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)
