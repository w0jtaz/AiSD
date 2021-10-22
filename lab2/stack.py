from linked_list import Node
from linked_list import LinkedList
from typing import Any

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        if not self._storage.head:
            return str(None)
        h: Node = self._storage.head
        reverse_list: LinkedList = LinkedList()
        out: str = ""
        reverse_list.push(self._storage.head.value)
        while h != self._storage.tail:
            h = h.next
            reverse_list.push(h.value)
        h = reverse_list.head
        out += str(reverse_list.head.value)
        while h != reverse_list.tail:
            h = h.next
            out += ('\n' + str(h.value))
        return out

    def __len__(self) -> int:
        return len(self._storage)

stack = Stack()

assert len(stack) == 0

stack.push(3)

assert str(stack) == '3'

stack.push(10)
stack.push(1)

assert str(stack) == '1\n10\n3'

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

print(stack)
print(stack.pop(),"\n")
print(stack)
print(len(stack))