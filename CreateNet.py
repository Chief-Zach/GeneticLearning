import Ball


class CreateNet:
    def __init__(self, balls, start, velocity):
        self.balls = balls
        self.ball_list = {}
        self.start = start
        self.velocity = velocity
        for i in range(self.balls):
            self.ball_list[i] = {'position': self.start, 'velocity': velocity}
