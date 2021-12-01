from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def isLeaf(self):
        return not (self.right_child or self.left_child)

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left_child is None:
                    self.left_child = BinaryNode(value)
                else:
                    self.left_child.add(value)
            elif value > self.value:
                if self.right_child is None:
                    self.right_child = BinaryNode(value)
                else:
                    self.right_child.add(value)
        else:
            self.value = value

class BinaryTree:
    root: BinaryNode



# tree = BinaryTree(10)