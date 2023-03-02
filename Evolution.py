import BallNet


class Evolution:
    def __init__(self, moves, number_of_balls, starting_pos, width, height, window, target):
        self.moves = moves
        self.generation_num = 0
        self.number_of_balls = number_of_balls
        self.starting_position = starting_pos
        self.moves = moves
        self.current_moves = 0
        self.fitness_values = {}
        self.sorted_keys = []
        self.width = width
        self.height = height
        self.window = window
        self.target = target
        self.balls = BallNet.BallNet(number_of_balls, [starting_pos[0], starting_pos[1]], width, height, window, target)

    def Generation(self):
        temp_balls = []
        genetics_saved = int(len(self.sorted_keys))
        for ball in range(genetics_saved):
            temp_balls.append(self.fitness_values[self.sorted_keys[ball]])
        self.balls.ball_list = temp_balls
        BallNet.BallNet(self.number_of_balls - genetics_saved, [self.starting_position[0], self.starting_position[1]],
                        self.width, self.height, self.window, self.target)

    def Step(self, frozen):
        if self.balls.dead_count < self.number_of_balls and self.current_moves <= self.moves:
            self.balls.move(int(self.generation_num), frozen)
            self.current_moves += 1 if not frozen else 0

        else:
            self.fitness_values, self.sorted_keys = self.balls.distance_function()
            print(f"Best Ball: {self.fitness_values[self.sorted_keys[0]]} with a value of {self.sorted_keys[0]}")
            self.fitness_values[self.sorted_keys[0]].colour = "GREEN"
            self.balls.freeze_pos()
            print("Generation complete")
            self.generation_num += 1
            print(self.fitness_values)
            self.balls.reset_pos()
            self.balls.dead_count = 0
            self.current_moves = 0
            self.Generation()
