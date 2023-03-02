import pygame
import Evolution
pygame.init()

window_w = 800
window_h = 600

black = (0, 0, 0)
white = (255, 255, 255)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Generation Learning")
clock = pygame.time.Clock()

number_of_balls = 1000

starting_moves = 500

target = [400, 100]

generation_saved = 20

mutation_rate = 1



def game_loop():
    velocity = [1, 1]
    pos_x = window_w / 2
    pos_y = window_h / 2

    running = True

    evolution = Evolution.Evolution(starting_moves, number_of_balls, [pos_x, pos_y], window_w, window_h, window, target)

    while running:
        freeze = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            freeze = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        evolution.Step(freeze)
        clock.tick(FPS)


game_loop()
