from dataclasses import dataclass
import typing as tp

@dataclass
class Node:

    next: tp.Optional[tp.Any]
    value: tp.Any


class LinkedList:

    _head: tp.Optional[Node]
    _current: tp.Any
    _size: int

    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._current = self._head

    def append(self, element: tp.Any) -> None:
        if self._size == 0:
            self._head = Node(None, element)
            self._current = self._head
            self._size += 1
        else:
            current_node = self._head
            while True:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    current_node.next = Node(None, element)
                    self._size += 1
                    break

    def __repr__(self):
        str_t = '['
        current = self._head
        while True:
            str_t += str(current.value)
            if current.next is not None:
                str_t += ', '
                current = current.next
            else:
                break

        str_t += ']'
        return str_t

    def __contains__(self, val: tp.Any):
        pass

    def __len__(self):
        return self._size

    def __iter__(self):
        return self

    def iteration(self, func):
        current = self._head

        if current is None:
            return

        while True:
            if current.next is not None:
                func(current)
                current = current.next
            else:
                break