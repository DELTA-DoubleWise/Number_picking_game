import numpy as np

class Game:
    def __init__(self, initial_states=(100,100,0,0), random_points=False):
        self.initial_states = initial_states
        self.random_points = random_points
        self.reset()

    def reset(self):
        if self.random_points:
            self.points = [np.random.randint(101), np.random.randint(101)]
        else:
            self.points = [self.initial_states[0], self.initial_states[1]]
        self.scores = [self.initial_states[2], self.initial_states[3]]
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
                    reward = int(reward / np.abs(reward)) if reward!=0 else 0
                    return self.get_state(), reward, True, winner
            return self.get_state(), 0, False, winner
        self.continuous_draw = 0
        self.points[0] -= actions[0]
        self.points[1] -= actions[1]
        self.scores[winner] += 1
        done = True if self.scores[winner] >= 4 else False
        reward = self.scores[0]-self.scores[1] if done else 0
        reward = int(reward / np.abs(reward)) if reward != 0 else 0
        return self.get_state(), reward, done, winner

    def get_state(self):
        return self.points[0], self.points[1], self.scores[0], self.scores[1]

