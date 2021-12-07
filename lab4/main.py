from typing import Any, List


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def isLeaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    # def add(self, value):
    #     if self.value:
    #         if value < self.value:
    #             if self.left_child is None:
    #                 self.left_child = BinaryNode(value)
    #             else:
    #                 self.left_child.add(value)
    #         elif value > self.value:
    #             if self.right_child is None:
    #                 self.right_child = BinaryNode(value)
    #             else:
    #                 self.right_child.add(value)
    #     else:
    #         self.value = value


def for_each_deep_first(node):
        if node:
            print(node.value)
            for_each_deep_first(node.left_child)
            for_each_deep_first(node.right_child)


def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.value == n2:
        return root

    left_child_lca = findLCA(root.left_child, n1, n2)
    right_child_lca = findLCA(root.right_child, n1, n2)

    if left_child_lca and right_child_lca:
        return root

    return left_child_lca if left_child_lca is not None else right_child_lca

class BinaryTree:
    root: BinaryNode


root = BinaryNode('F')

root.left_child = BinaryNode('B')
root.right_child = BinaryNode('G')
root.left_child.left_child = BinaryNode('A')
root.left_child.right_child = BinaryNode('D')
root.right_child.right_child = BinaryNode('I')
root.left_child.right_child.left_child = BinaryNode('C')
root.left_child.right_child.right_child = BinaryNode('E')
root.right_child.right_child = BinaryNode('I')
root.right_child.right_child.left_child = BinaryNode('H')

for_each_deep_first(root)
print("\n")

for_each_deep_first(root.left_child)
print("\n")

for_each_deep_first(root.right_child)
print("\n")

for_each_deep_first(root.left_child.right_child)
print("\n")

for_each_deep_first(root.right_child.left_child)

print(root.isLeaf())
