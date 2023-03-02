import random
import pygame
import Ball


class BallNet:
    def __init__(self, balls, start, width, height, window):
        self.balls = balls
        self.ball_list = []
        self.position = start
        self.velocity = [0, 0]
        self.width = width
        self.height = height
        self.window = window
        self.dead_count = 0
        for i in range(self.balls):
            self.ball_list.append(Ball.Ball(self.window, self.position[0] + i/100000, self.position[1] + i/10000))

    def move(self):
        for ball_num, current_ball in enumerate(self.ball_list):
            print(current_ball)
            if not current_ball.dead:
                self.velocity = [random.randrange(-1, 2), random.randrange(-1, 2)]
                print(self.velocity)
                current_ball.pos_x += self.velocity[0]
                current_ball.pos_y += self.velocity[1]

                if self.position[0] + 5 > self.width or self.position[0] < 0:
                    self.velocity[0] = -self.velocity[0]
                    print("X direction violated")
                    current_ball.kill()

                if self.position[1] + 5 > self.height or self.position[1] < 0:
                    self.velocity[1] = -self.velocity[1]
                    print("Y direction violated")
                    current_ball.kill()

                print(f"Drawing Ball {ball_num}")
                print(f"Current Ball Postion: {current_ball.pos_x, current_ball.pos_y}")
                current_ball.draw()
            else:
                self.dead_count += 1
                if self.dead_count == self.balls:
                    pygame.quit()
                    quit()

