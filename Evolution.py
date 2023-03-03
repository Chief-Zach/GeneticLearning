import random
import time

import pygame.time

import BallNet


class Evolution:
    def __init__(self, moves, number_of_balls, starting_pos, width, height, window, target, genetics_saved,
                 mutation_rate, min_man_velocity):
        self.generational_winners = None
        self.saved_balls = None
        self.generation_num = 0
        self.number_of_balls = number_of_balls
        self.starting_position = starting_pos
        self.moves = moves
        self.current_moves = 0
        self.sorted_fitness = {}
        self.sorted_keys = []
        self.width = width
        self.height = height
        self.window = window
        self.target = target
        self.genetics_saved = genetics_saved / 100
        self.mutation_rate = mutation_rate / 100
        self.min_max_velocity = min_man_velocity
        self.balls = BallNet.BallNet(number_of_balls, [starting_pos[0], starting_pos[1]], width, height, window, target,
                                     self.generation_num, self.moves, self.min_max_velocity)
        self.balls.create_net()

    def Generation(self):
        self.generational_winners = []
        self.saved_balls = int(self.number_of_balls * self.genetics_saved)

        print(f"Saving {self.saved_balls} Genetics")
        self.balls = BallNet.BallNet(self.number_of_balls - self.saved_balls, [self.starting_position[0],
                                                                               self.starting_position[1]], self.width,
                                     self.height, self.window, self.target, self.generation_num, self.moves, self.min_max_velocity)

        for ball in range(self.saved_balls):
            current_ball = list(self.sorted_fitness)[ball]

            self.generational_winners.append(current_ball)
            if len(current_ball.saved_moves) < 1:
                current_ball.saved_moves = current_ball.generational_moves
                current_ball.generational_moves = []

        self.Create_Children(self.number_of_balls - self.saved_balls)
        pygame.time.delay(1000)
        self.balls.ball_list += self.generational_winners
        print(f"Currently {len(self.balls.ball_list)} in the array")

    def Create_Children(self, number_of_children):
        print(f"Generating: {number_of_children}")
        for _ in range(number_of_children):
            self.balls.create_ball(self.Mutation(self.Crossover()))

    def Crossover(self):
        random_num1 = random.randrange(0, len(self.generational_winners))
        random_num2 = random.randrange(0, len(self.generational_winners))

        starting_velocities = self.generational_winners[random_num1].saved_moves[0:int(self.moves / 2) + 1]
        ending_velocities = self.generational_winners[random_num2].saved_moves[int(self.moves / 2) + 1:]
        child_velocity = starting_velocities + ending_velocities
        return child_velocity

    def Mutation(self, child):
        mutation_per = int(self.moves * self.mutation_rate)
        for x in random.sample(range(self.moves), mutation_per):
            child[x] = [random.randrange(-self.min_max_velocity, self.min_max_velocity + 1), random.randrange(-self.min_max_velocity, self.min_max_velocity + 1)]
        return child

    def Step(self, frozen, hidden):
        if self.balls.dead_count < self.number_of_balls and self.current_moves < self.moves:
            self.balls.move(int(self.generation_num), self.current_moves, frozen, hidden)
            self.current_moves += 1 if not frozen else 0

        else:
            self.sorted_fitness, self.sorted_keys = self.balls.distance_function()
            print(f"Best Ball: {self.sorted_keys[0]} with a value of {self.sorted_fitness[self.sorted_keys[0]]}")
            print(list(self.sorted_fitness)[0].saved_moves)
            self.balls.reset_pos()
            list(self.sorted_fitness)[0].best_ball = True
            print("Generation complete")
            self.generation_num += 1
            self.balls.dead_count = 0
            self.current_moves = 0
            self.Generation()
