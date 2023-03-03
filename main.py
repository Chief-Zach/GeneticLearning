import random

import pygame
import Evolution

pygame.init()

window_w = 1800
window_h = 800

black = (0, 0, 0)
white = (255, 255, 255)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Generation Learning")
clock = pygame.time.Clock()

number_of_balls = 1000

starting_moves = 500

min_max_velocity = 5

target = [random.randrange(window_w), random.randrange(window_h)]

generation_saved = 20

mutation_rate = 2

starting_x = window_w / 2
starting_y = window_h / 2

def game_loop():
    hidden = False

    running = True

    evolution = Evolution.Evolution(starting_moves, number_of_balls, [starting_x, starting_y], window_w, window_h, window, target,
                                    generation_saved, mutation_rate, min_max_velocity)

    while running:
        freeze = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            freeze = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if not hidden:
                        hidden = True
                    else:
                        hidden = False

        evolution.Step(freeze, hidden)
        clock.tick(FPS)


game_loop()
