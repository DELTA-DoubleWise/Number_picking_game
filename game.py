import numpy as np

class Game:
    def __init__(self, initial_points=100):
        self.initial_points = initial_points
        self.reset()

    def reset(self):
        self.points = [self.initial_points, self.initial_points]
        self.scores = [0, 0]
        self.rounds = 0
        self.action_space = list(range(101))
        self.continuous_draw = 0
        return self.get_state()

    def step(self, actions):
        winner = -1
        if actions[0] > actions[1]:
            winner = 0
        elif actions[1] > actions[0]:
            winner = 1
        else:  # draw
            self.continuous_draw+=1
            if self.points[0]==0 or self.continuous_draw==5:
                if self.scores[0] == self.scores[1]:
                    return self.get_state(), 0, True, 2
                else:
                    winner = 0 if self.scores[0]>self.scores[1] else 1
                    reward = self.scores[0]-self.scores[1]
                    return self.get_state(), reward, True, winner
            return self.get_state(), 0, False, winner
        self.continuous_draw = 0
        self.points[0] -= actions[0]
        self.points[1] -= actions[1]
        self.scores[winner] += 1
        self.rounds += 1
        done = True if self.scores[winner] >= 4 else False
        reward = self.scores[0]-self.scores[1] if done else 0
        return self.get_state(), reward, done, winner

    def get_state(self):
        return self.points[0], self.points[1], self.scores[0], self.scores[1]

