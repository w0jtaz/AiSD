from typing import Any

class Node:
    value: Any
    next: 'Node'

class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        new: Node = Node()
        new.value = value
        new.next = self.head
        if not self.tail:
            self.tail = new
        self.head = new

    def append(self, value: Any) -> None:
        new: Node = Node()
        new.value = value
        new.next = None
        if not self.head:
            self.head = new
        if self.tail:
            self.tail.next = new
        self.tail = new

    def node(self, at: int) -> Node:
        if not self.head:
            return None
        curr: Node = self.head
        curr_i: int = 0
        while curr_i < at:
            if not curr.next:
                return None
            curr = curr.next
            curr_i += 1
        return curr

    def insert(self, value: Any, after: Node) -> None:
        if not after:
            pass
        else:
            new: Node = Node()
            new.value = value
            between: Node = after.next
            if after == self.tail:
                self.tail = new
            new.next = between
            after.next = new

    def pop(self) -> Node:
        popped: Node = self.head
        self.head = popped.next
        popped.next = None
        return popped.value

    def remove_last(self) -> Node:
        length = len(self)
        last: Node = self.tail
        if length <= 1:
            self.tail = None
            self.head = None
            return last
        self.tail = self.node(len(self)-2)
        self.tail.next = None
        return last.value

    def remove(self, after: Node) -> None:
        removed: Node = after.next
        if removed.next:
            after.next = removed.next
        else:
            self.tail = after
        removed.next = None

    def __str__(self) -> str:
        if not self.head:
            return str(None)
        h: Node = self.head
        out: str = ""
        out += str(self.head.value)

        while h != self.tail:
            h = h.next
            out += (' -> ' + str(h.value))
        return out

    def __len__(self) -> int:
        if not self.head:
            return 0
        ln: int = 1
        h: Node = self.head
        while h != self.tail:
            ln += 1
            h = h.next
        return ln


list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

# print(list_.remove_last())
# print(list_)
# print(len(list_))

