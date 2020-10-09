class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def _insert(self, value, cur_node):
        if value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                return value
            self._insert(value, cur_node.right)
            return value
        elif value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                return value
            self._insert(value, cur_node.left)
            return value
        return "The Element" + str(value) + "Already Exists"

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return value
        self._insert(value, self.root)

    def _if_exist(self, value, cur_node):
        if value > cur_node.value:
            return self._if_exist(value, cur_node.right)
        elif value < cur_node.value:
            return self._if_exist(value, cur_node.left)
        else:
            return True

    def if_exist(self, value):
        if self.root is None:
            return False
        if value == self.root:
            return True
        found = self._if_exist(value, self.root)
        if found:
            return True
        return False
