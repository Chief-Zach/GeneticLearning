import BallNet


class Evolution:
    def __init__(self, moves, number_of_balls, starting_pos, width, height, window, target):
        self.moves = moves
        self.generation_num = 0
        self.number_of_balls = number_of_balls
        self.moves = moves
        self.current_moves = 0
        self.fitness_values = {}
        self.balls = BallNet.BallNet(number_of_balls, [starting_pos[0], starting_pos[1]], width, height, window, target)

    def Generation(self, frozen=False):
        if self.balls.dead_count < self.number_of_balls and self.current_moves <= self.moves:
            self.balls.move(frozen)
            self.current_moves += 1 if not frozen else 0

        else:
            self.balls.freeze_pos()
            print("Generation complete")
            self.fitness_values, sorted_keys = self.balls.distance_function()
            print(self.fitness_values)
            print(f"Best Ball: {self.fitness_values[sorted_keys[0]]} with a value of {sorted_keys[0]}")
            self.balls.reset_pos()
            self.balls.dead_count = 0
            self.current_moves = 0
