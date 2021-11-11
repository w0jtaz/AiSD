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
        stack = ""
        if self._storage.head is None:
            return str(None)
        i = self._storage.head
        reverse_list: LinkedList = LinkedList()
        reverse_list.push(self._storage.head.value)
        while i != self._storage.tail:
            i = i.next
            reverse_list.push(i.value)
        i = reverse_list.head
        stack += str(reverse_list.head.value)
        while i != reverse_list.tail:
            i = i.next
            stack += ('\n' + str(i.value))
        return stack

    def __len__(self) -> int:
        return len(self._storage)

stack = Stack()
print(stack)

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
print("\n")
print(stack.pop())
print("\n")
print(stack)
print("\n")
print(len(stack))