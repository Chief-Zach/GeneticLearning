import random
import pygame
import Ball
import Evolution

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

ball_colours = ["BLACK", "GREEN", "RED", "ORANGE", "YELLOW" , "TURQUOISE", "BLUE"]

class BallNet:
    def __init__(self, balls, start, width, height, window, target):
        self.generation = 0
        self.balls = balls
        self.ball_list = []
        self.position = start
        self.starting_position = start
        self.velocity = [0, 0]
        self.width = width
        self.height = height
        self.window = window
        self.dead_count = 0
        self.target = target
        for i in range(self.balls):
            self.ball_list.append(Ball.Ball(self.window, self.position[0] + i / 100000, self.position[1] + i / 10000))

    def move(self, generation, frozen=False):
        self.generation = generation
        self.window.fill(white)

        font = pygame.font.Font('freesansbold.ttf', 20)

        text = font.render(f"Generation: {str(int(generation))}", True, black, white)

        textRect = text.get_rect()

        textRect.center = (75, 50)

        self.window.blit(text, textRect)

        pygame.draw.circle(self.window, red, self.target, 5)
        if frozen:
            self.freeze_pos()
            pygame.display.update()
            print("Freezing")
            return 0

        for ball_num, current_ball in enumerate(self.ball_list):
            if not current_ball.dead:
                self.velocity = [random.randrange(-1, 2), random.randrange(-1, 2)]
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

                current_ball.draw(current_ball.colour)
        pygame.display.update()

    def freeze_pos(self):
        for current_ball in self.ball_list:
            current_ball.draw(current_ball.colour, True)

    def reset_pos(self):
        for ball_num, current_ball, in enumerate(self.ball_list):
            current_ball.pos_x = self.starting_position[0]
            current_ball.pos_y = self.starting_position[1]
            current_ball.colour = ball_colours[self.generation]
            current_ball.dead = False

    def distance_function(self):
        distance_list = {}
        for ball in self.ball_list:
            distance = ((self.target[0] - ball.pos_x) ** 2 + (self.target[1] - ball.pos_y) ** 2) ** 1 / 2
            distance_list[distance] = ball
        sorted_keys = sorted(distance_list)
        return distance_list, sorted_keys
