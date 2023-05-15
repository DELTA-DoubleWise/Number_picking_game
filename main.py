from game import Game
from agent import QLearningAgent
from numpy import nper

def main():
    params = {
        "discount_factor": 0.95,
        "epsilon": 0.5,
        "epsilon_decay": 1,
        "min_epsilon": 0.01,
        "learning_rate": 0.1,
        "min_learning_rate": 0.01,
        "learning_rate_decay": 1,
    }

    game = Game()
    agent = QLearningAgent(game, params)
    agent.run(1000000, True)
    eval_rs = agent.run(10, False)

if __name__ == "__main__":
    main()