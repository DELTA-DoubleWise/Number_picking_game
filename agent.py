import numpy as np
from game import Game
from typing import Dict, Any, Tuple, Callable
import numpy.typing as npt

class QLearningAgent():
    def __init__(self, env, params: Dict[str, Any]):
        self.env = env
        self.params = params
        self.policy = {}

        self.lr = self.params["learning_rate"]
        self.min_lr = self.params["min_learning_rate"]
        self.lr_decay = self.params["learning_rate_decay"]
        self.gamma = self.params["discount_factor"]
        self.eps = self.params["epsilon"]
        self.eps_decay = self.params["epsilon_decay"]
        self.min_eps = self.params["min_epsilon"]

    def get_action(self, state: npt.NDArray, train: bool) -> int:
        """Return an action given the current state"""
        # YOUR CODE HERE
        if state not in self.policy:
            self.policy[state] = {i: 0.0 for i in range(state[0] + 1)}

        if train:
            if np.random.random_sample()<self.eps:
                return np.random.choice(list(self.policy[state].keys()))

        max_Q = -float(np.inf)
        action = 0
        if max(self.policy[state].values()) == min(self.policy[state].values()):
            action = np.random.choice(list(self.policy[state].keys()))
        else:
            for i in range(self.env.points[0]):
                if self.policy[state][i] > max_Q:
                    max_Q = self.policy[state][i]
                    action = i
        return action

    def step(self, actions: list) -> Tuple[npt.NDArray, float, bool, int]:
        next_state, reward, done, winner = self.env.step(actions)
        return next_state, reward, done, winner

    def learn(
        self, state: npt.NDArray, action: int, reward: float, next_state: npt.NDArray
    ) -> float:
        """Update Agent's policy using the Q-learning algorithm and return the update delta"""
        # YOUR CODE HERE
        next_action = self.get_action(next_state, False)
        td = reward+self.gamma*self.policy[next_state][next_action]-self.policy[state][action]
        self.policy[state][action] = td*self.lr + self.policy[state][action]
        return td

    def run(self, max_episodes: int, train: bool):
        # YOUR CODE HERE
        episode_rewards = dict()
        total_rewards = 0

        for ne in range(max_episodes):
            state = self.env.reset()
            done = False
            total_reward = 0
            winner = -1
            while not done:
                # print(state)
                if not train:
                    print(state)
                action = self.get_action(state, train)
                if train:
                    next_state, reward, done, winner = self.step([action, np.random.choice(self.env.points[1]+1)])
                else:
                    op_action = int(input("Please enter your choice: "))
                    next_state, reward, done, winner = self.step([action, op_action])

                if next_state not in self.policy:
                    self.policy[next_state] = {i: 0.0 for i in range(next_state[0] + 1)}

                if train:
                    self.learn(state, action, reward, next_state)

                state = next_state

                total_reward += reward

                # if not train and done:
                if not train and done:
                    if winner == 0:
                        print("Computer wins")
                    elif winner == 1:
                        print("You win")
                    elif winner == 2:
                        print("Draw")

            episode_rewards[ne] = total_reward
            total_rewards += total_reward
            print(f"episode {ne}: {total_reward}")

            self.eps = max(self.eps*self.eps_decay, self.min_eps)
            self.lr = max(self.lr*self.lr_decay, self.min_lr)
        print("total rewards: ", total_rewards)

        return episode_rewards