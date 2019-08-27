class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child_val):
        subtree = self.pop(1)
        if len(subtree) > 1:
            self.insert(1, [child_val, subtree, []])
        else:
            self.insert(1, [child_val, [], []])

    def insert_right(self, child_val):
        subtree = self.pop(2)
        if len(subtree) > 1:
            self.insert(2, [child_val, [], subtree])
        else:
            self.insert(2, [child_val, [], []])
        return self

    def get_self_val(self):
        return self[0]

    def set_self_val(self, new_val):
        self[0] = new_val

    def get_left_child(self):
        return self[1]

    def get_right_child(self):
        return self[2]

    # def insert_left(self, child):
    #     if self.left is None:
    #         self.left = child
    #     else:
    #         child.left = self.left
    #         self.left = child
    #
    # def insert_right(self, child):
    #     if self.right is None:
    #         self.right = child
    #     else:
    #         child.right = self.right
    #         self.right = child
