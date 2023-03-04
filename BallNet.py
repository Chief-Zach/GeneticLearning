import random
import pygame
import Ball
import Evolution

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (18, 18, 18)
ball_colours = ["GREEN", "RED", "ORANGE", "YELLOW", "TURQUOISE", "BLUE"]


class BallNet:
    def __init__(self, balls, start, width, height, window, target, generation, total_moves, min_max_velocity):
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
        self.total_moves = total_moves
        self.min_max_velocity = min_max_velocity

    def move(self, generation, move, best_score, frozen=False, hidden=False):
        self.generation = generation
        self.window.fill(grey)

        font = pygame.font.Font('freesansbold.ttf', 20)

        true_distance = best_score

        if best_score <= self.total_moves:
            true_distance = 0
        elif best_score > self.total_moves:
            true_distance = round((best_score - self.total_moves)**(1/5), 2)

        generation_text = font.render(f"Generation: {str(generation + 1)}", True, black, white)
        best_score_text = font.render(f"Best Distance: {str(true_distance) if true_distance != -1 else 'None'}", True, black, white)
        best_moves_text = font.render(f"Best Moves: {str(best_score) if (best_score-self.total_moves) <= 0 and best_score != 0 else 'Unsolved'}", True, black, white)

        generation_box = generation_text.get_rect()
        best_score_box = best_score_text.get_rect()
        best_moves_box = best_score_text.get_rect()

        generation_box.topleft = (75, 50)
        best_score_box.topleft = (75, 70)
        best_moves_box.topleft = (75, 90)

        self.window.blit(generation_text, generation_box)
        self.window.blit(best_score_text, best_score_box)
        self.window.blit(best_moves_text, best_moves_box)

        pygame.draw.circle(self.window, white, self.target, 20)
        if frozen:
            self.freeze_pos()
            pygame.display.update()
            return 0
        for ball_num, current_ball in enumerate(self.ball_list):
            if not current_ball.dead:
                if 0 < len(current_ball.saved_moves) > move:
                    current_ball.pos_x += current_ball.saved_moves[move][0]
                    current_ball.pos_y += current_ball.saved_moves[move][1]

                else:
                    self.velocity = [random.randrange(-self.min_max_velocity, self.min_max_velocity + 1), random.randrange(-self.min_max_velocity, self.min_max_velocity + 1)]
                    current_ball.current_vector = self.velocity
                    current_ball.pos_x += self.velocity[0]
                    current_ball.pos_y += self.velocity[1]

                if current_ball.pos_x + 5 > self.width or current_ball.pos_x < 0:
                    current_ball.kill()
                    self.dead_count += 1

                elif current_ball.pos_y + 5 > self.height or current_ball.pos_y < 0:
                    current_ball.kill()
                    self.dead_count += 1

                if hidden and generation != 0:
                    if current_ball.best_ball:
                        current_ball.draw(current_ball.colour)
                else:
                    current_ball.draw(current_ball.colour)
                current_ball.move = move
        pygame.display.update()
        return self.dead_count

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
            if not ball.dead:
                distance = ((self.target[0] - ball.pos_x) ** 2 + (self.target[1] - ball.pos_y) ** 2) ** (1/2)
                final_function = distance**5
                distance_list[ball] = final_function + ball.move
            else:
                distance_list[ball] = self.width**6
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
