import treelib
from typing import Any, Callable

# binarny węzeł drzewa przechowujący wartość oraz lewe i prawe dziecko.
class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    # inicjalizator ustawia wartość bieżącego węzła
    def __init__(self, value=Any) -> None:
        self.left_child = None
        self.right_child = None
        self.value = value

    # przesłonięcie metody w celu uzyskania wartości
    def __str__(self):
        return str(self.value)

    # is_leaf() sprawdza czy węzeł jest liściem
    def is_leaf(self):
        if (self.right_child == None) and (self.left_child == None):
            return True
        else:
            return False

    # add_left_child dodaje lewe dziecko bieżącego węzła jako nowy węzeł
    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    # add_right_child dodaje prawe dziecko bieżącego węzła jako nowy węzeł
    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    # traverse_post_order wykonuje operację wstecznego przejscia po podrzędnych węzłach
    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach
    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

# przechowuje strukturę drzewa binarnego
class BinaryTree:
    root: BinaryNode

    # inicjalizator, root reprezentuje węzeł będący korzeniem
    def __init__(self, value= Any):
        self.root = BinaryNode(value)

    # traverse_in_order wykonuje operację poprzecznego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    # traverse_post_order wykonuje operację wstecznego przejscia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    # wyświetla drzewo w formie graficznej
    def show(self) -> None:
        binary_tree = treelib.Tree()
        binary_tree.create_node(str(self.root.value), str(self.root.value))

        def binary_children(node: 'BinaryNode'):
            if node.left_child != None:
                binary_tree.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child != None:
                binary_tree.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.traverse_pre_order(binary_children)
        binary_tree.show()

# zwraca najbliższy wspólny węzeł nadrzędny przekazanych węzłów first_node->n1 , second_node ->n2
def closest_parent(binary_tree: BinaryTree, n1: BinaryNode, n2: BinaryNode) -> BinaryNode:
    if binary_tree == n1 or binary_tree == n2:
        return binary_tree
    elif binary_tree == None:
        return None

    left = closest_parent(binary_tree.left_child, n1, n2)
    right = closest_parent(binary_tree.right_child, n1, n2)

    if left != None and right != None:
        return binary_tree
    elif left != None:
        return left
    else:
        return right


# wartość w korzeniu drzewa wynosi 10
binary_tree = BinaryTree(10)
binary_tree.root.add_left_child(8)
binary_tree.root.add_right_child(2)
binary_tree.root.left_child.add_left_child(1)
binary_tree.root.left_child.add_right_child(5)
binary_tree.root.right_child.add_left_child(4)
binary_tree.root.right_child.add_right_child(7)

# drukujemy drzewo na ekran
binary_tree.show()

# wyszukiwanie nadrzędnego węzła dla pary (2,8)
print("Closest parent of (2,8): ",closest_parent(binary_tree.root, binary_tree.root.right_child, binary_tree.root.left_child))

# wyszukiwanie nadrzędnego węzła dla pary (1,5)
print("Closest parent of (1,5): ",closest_parent(binary_tree.root, binary_tree.root.left_child.left_child, binary_tree.root.left_child.right_child))

# wyszukiwanie nadrzędnego węzła dla pary (4,7)
print("Closest parent of (4,7): ",closest_parent(binary_tree.root, binary_tree.root.right_child.left_child, binary_tree.root.right_child.right_child))

# testy poprawności implementacji
assert binary_tree.root.value == 10
assert binary_tree.root.right_child.value == 2
assert binary_tree.root.right_child.is_leaf() is False
assert binary_tree.root.left_child.left_child.value == 1
assert binary_tree.root.left_child.left_child.is_leaf() is True
