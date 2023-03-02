import time

import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, window, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.window = window
        self.dead = False
        self.past_moves = []
        # self.velocity = [randint(4, 8), randint(-8, 8)]

    def draw(self):
        self.past_moves.append([self.pos_x, self.pos_y])
        pygame.draw.circle(self.window, BLACK, [self.pos_x, self.pos_y], 5)

    def kill(self):
        self.dead = True
