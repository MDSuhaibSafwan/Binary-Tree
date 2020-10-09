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


tree = BinaryTree()
tree.insert(8)
tree.insert(10)
tree.insert(5)
tree.insert(6)
tree.insert(4)
