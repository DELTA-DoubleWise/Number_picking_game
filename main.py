from game import Game
from agent import QLearningAgent, pick_action
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
    # with open('model_10choice.pickle', 'wb') as f:
    #     pickle.dump(policy, f, protocol=pickle.HIGHEST_PROTOCOL)
    # plot_reward(episode_reward, "training_reward_10choice.png")
    with open('model_10choice.pickle', 'rb') as f:
        policy_1 = pickle.load(f)
    with open('model.pickle', 'rb') as f:
        policy_2 = pickle.load(f)
    eval_agent = QLearningAgent(game,params,policy_2)
    agent = QLearningAgent(game,params,policy_1)
    eval_rs = agent.run(1000, False, "model", eval_agent)

if __name__ == "__main__":
    main()