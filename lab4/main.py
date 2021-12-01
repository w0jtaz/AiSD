from typing import Any, List


class TreeNode:
    value: Any

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def isLeaf(self):
        return not (self.right or self.left)

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

def for_each_deep_first(node):
        if node:
            print(node.value)
            for_each_deep_first(node.left)
            for_each_deep_first(node.right)

class Tree:
    root: TreeNode



root = TreeNode('F')

root.left = TreeNode('B')
root.right = TreeNode('G')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.right.right = TreeNode('I')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')

for_each_deep_first(root)
print("\n")

for_each_deep_first(root.left)
print("\n")

for_each_deep_first(root.right)
print("\n")

for_each_deep_first(root.left.right)
print("\n")

for_each_deep_first(root.right.left)






