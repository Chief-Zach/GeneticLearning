import random
import pygame
import Ball
import Evolution

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

ball_colours = ["GREEN", "RED", "ORANGE", "YELLOW", "TURQUOISE", "BLUE"]


class BallNet:
    def __init__(self, balls, start, width, height, window, target, generation):
        self.generation = generation
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

    def move(self, generation, move, frozen=False):
        self.generation = generation
        self.window.fill(white)

        font = pygame.font.Font('freesansbold.ttf', 20)

        text = font.render(f"Generation: {str(int(generation))}", True, black, white)

        textRect = text.get_rect()

        textRect.center = (75, 50)

        self.window.blit(text, textRect)

        pygame.draw.circle(self.window, black, self.target, 20)
        if frozen:
            self.freeze_pos()
            pygame.display.update()
            print("Freezing")
            return 0
        for ball_num, current_ball in enumerate(self.ball_list):
            if not current_ball.dead:
                if 0 < len(current_ball.saved_moves) > move:
                    current_ball.pos_x += current_ball.saved_moves[move][0]
                    current_ball.pos_y += current_ball.saved_moves[move][1]

                else:
                    self.velocity = [random.randrange(-1, 2), random.randrange(-1, 2)]
                    current_ball.current_vector = self.velocity
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
            current_ball.dead = False
            current_ball.best_ball = False

    def distance_function(self):
        distance_list = {}
        for ball in self.ball_list:
            distance = ((self.target[0] - ball.pos_x) ** 2 + (self.target[1] - ball.pos_y) ** 2) ** 1 / 2
            distance_list[ball] = distance
        sorted_dict = dict(sorted(distance_list.items(), key=lambda item: item[1]))
        sorted_keys = list(sorted_dict.keys())
        return sorted_dict, sorted_keys

    def create_net(self):
        for i in range(self.balls):
            self.ball_list.append(Ball.Ball(self.window, self.starting_position[0], self.starting_position[1],
                                            ball_colours[self.generation % 6]))
        print(f"Currently {len(self.ball_list)} in the array")


    def create_ball(self, saved_moves):
        self.ball_list.append(Ball.Ball(self.window, self.starting_position[0], self.starting_position[1],
                                        ball_colours[self.generation % 6], saved_moves))
