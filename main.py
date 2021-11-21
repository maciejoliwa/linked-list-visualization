import typing as tp
import pygame
from pygame.locals import *
from linked_list import LinkedList, Node


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
