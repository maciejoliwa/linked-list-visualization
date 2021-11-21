from dataclasses import dataclass
import typing as tp
import pygame
from pygame.locals import *


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


def main():
    ls = LinkedList()
    pygame.init()

    FPS = pygame.time.Clock()

    display = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("LINKED LIST VISUALIZATION")

    def draw_point(el: Node):
        pygame.draw.circle(
            display,
            (0, 0, 0),
            center=(el.value['x'], el.value['y']),
            radius=5,
            width=5
        )

    def draw_line(el: Node):
        pygame.draw.aaline(
            display,
            (255, 0, 0),
            (el.value['x'], el.value['y']),
            (el.next.value['x'], el.next.value['y']),
            blend=3
        )

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                x, y = position[0], position[1]
                ls.append({ 'x': x, 'y': y })
                draw_point(Node(None, { 'x': x , 'y': y}))
            elif event.type == KEYDOWN:
                ls._head = None
                ls._size = 0

        display.fill((255, 255, 255))
        ls.iteration(draw_line)
        ls.iteration(draw_point)
        pygame.display.update()
        FPS.tick(60)


main()
