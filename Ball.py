import time

import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 0, 0)
TURQUOISE = (0, 255, 255)
BLUE = (0, 255, 255)


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, window, pos_x, pos_y, colour, saved_moves=[]):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.window = window
        self.dead = False
        self.saved_moves = saved_moves
        self.generational_moves = []
        self.colour = colour
        self.best_ball = False
        self.current_vector = []
        self.move = 0

    def draw(self, colour, frozen=False):
        match colour:
            case "BLACK":
                colour = BLACK
            case "GREEN":
                colour = GREEN
            case "RED":
                colour = RED
            case "ORANGE":
                colour = ORANGE
            case "YELLOW":
                colour = YELLOW
            case "TURQUOISE":
                colour = TURQUOISE
            case "BLUE":
                colour = BLUE

        if not frozen:
            self.generational_moves.append(self.current_vector)
        pygame.draw.circle(self.window, colour, [self.pos_x, self.pos_y], 5)

    def kill(self):
        self.dead = True
