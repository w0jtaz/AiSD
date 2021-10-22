from linked_list import Node
from linked_list import LinkedList
from typing import Any

class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, value) -> None:
        self._storage.append(value)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        if not self._storage.head:
            return str(None)
        h: Node = self._storage.head
        out: str = ""
        out += str(self._storage.head.value)

        while h != self._storage.tail:
            h = h.next
            out += (', ' + str(h.value))
        return out

    def __len__(self) -> int:
        return len(self._storage)

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
queue.enqueue('klient4')
queue.enqueue('klient5')

assert str(queue) == 'klient1, klient2, klient3, klient4, klient5'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3, klient4, klient5'
assert len(queue) == 4

print(len(queue))

print(queue.peek())
queue.dequeue()
print(queue.peek())

print(len(queue))

print(queue)