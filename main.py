from game import Game
from agent import QLearningAgent
from numpy import nper
from utils import plot_reward
import pickle

def main():
    params = {
        "discount_factor": 0.95,
        "epsilon": 0.5,
        "epsilon_decay": 1,
        "min_epsilon": 0.001,
        "learning_rate": 0.1,
        "min_learning_rate": 0.001,
        "learning_rate_decay": 1,
    }

    game = Game()
    # agent = QLearningAgent(game, params)
    # episode_reward, policy = agent.run(5000000, True)
    # with open('model.pickle', 'wb') as f:
    #     pickle.dump(policy, f, protocol=pickle.HIGHEST_PROTOCOL)
    # plot_reward(episode_reward)
    with open('model.pickle', 'rb') as f:
        policy = pickle.load(f)
    agent = QLearningAgent(game,params,policy)
    eval_rs = agent.run(10, False)

if __name__ == "__main__":
    main()