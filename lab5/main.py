from typing import Any, Callable
import treelib


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value=Any) -> None:
        self.left_child = None
        self.right_child = None
        self.value = value

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if (self.right_child is None) and (self.left_child is None):
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value= Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)


    def show(self) -> None:
        binary_tree = treelib.Tree()
        binary_tree.create_node(str(self.root.value), str(self.root.value))

        def createShow(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                binary_tree.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child is not None:
                binary_tree.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.traverse_pre_order(createShow)
        binary_tree.show()

def closest_parent(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> BinaryNode:
    if tree is first_node or tree is second_node:
        return tree
    elif tree is None:
        return None

    left = closest_parent(tree.left_child, first_node, second_node)
    right = closest_parent(tree.right_child, first_node, second_node)

    if left is not None:
        return left
    elif right is not None and left is not None:
        return tree
    else:
        return right



binary_tree = BinaryTree(10)
binary_tree.root.add_left_child(9)
binary_tree.root.add_right_child(2)
binary_tree.root.left_child.add_left_child(1)
binary_tree.root.left_child.add_right_child(4)
binary_tree.root.right_child.add_left_child(3)
binary_tree.root.right_child.add_right_child(6)

binary_tree.show()
print(closest_parent(binary_tree.root, binary_tree.root.left_child.right_child, binary_tree.root.left_child.left_child.left_child))

assert binary_tree.root.value == 10
assert binary_tree.root.right_child.value == 2
assert binary_tree.root.right_child.is_leaf() is False
assert binary_tree.root.left_child.left_child.value == 1
assert binary_tree.root.left_child.left_child.is_leaf() is True

