from typing import Any,Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value=Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
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


bin_node1 = BinaryNode("X")
bin_node1.add_left_child("Y")
bin_node1.add_right_child("Z")

print(bin_node1)
print(bin_node1.left_child)
print(bin_node1.right_child)

print(bin_node1.is_leaf())
print(bin_node1.left_child.is_leaf())
print(bin_node1.right_child.is_leaf())

print(bin_node1.traverse_in_order)
print(bin_node1.traverse_post_order)
print(bin_node1.traverse_pre_order)