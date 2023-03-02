import pygame
import Ball
import BallNet

pygame.init()

window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Game: ")
clock = pygame.time.Clock()

number_of_balls = 1000


def game_loop():
    block_size = 20

    velocity = [1, 1]
    saved_velocity = velocity
    pos_x = window_w / 2
    pos_y = window_h / 2

    Balls = BallNet.BallNet(number_of_balls, [pos_x, pos_y], window_w, window_h, window)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    saved_velocity = velocity
                    velocity = [0, 0]
            if event.type == pygame.KEYUP:
                velocity = saved_velocity

        pos_x += velocity[0]
        pos_y += velocity[1]

        if pos_x + block_size > window_w or pos_x < 0:
            velocity[0] = -velocity[0]

        if pos_y + block_size > window_h or pos_y < 0:
            velocity[1] = -velocity[1]

        # DRAW
        window.fill(white)
        Balls.move()
        pygame.draw.circle(window, red, [400, 100], 5)
        pygame.display.update()
        clock.tick(FPS)


game_loop()
