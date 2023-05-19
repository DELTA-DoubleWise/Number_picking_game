from game import Game
from agent import QLearningAgent, pick_action
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
    # with open('model_reward_1.pickle', 'rb') as f:
    #     policy_1 = pickle.load(f)
    # agent = QLearningAgent(game, params, policy_1)
    agent = QLearningAgent(game, params)
    episode_reward, policy = agent.run(500000, True)

    with open('models/model_bottom_up.pickle', 'wb') as f:
        pickle.dump(policy, f, protocol=pickle.HIGHEST_PROTOCOL)
    # plot_reward(episode_reward, "training_reward_reward_2.png")

    # with open('models/model_10choice_15m.pickle', 'rb') as f:
    #     policy = pickle.load(f)
    # eval_agent = QLearningAgent(game,params,policy_2)
    # agent = QLearningAgent(game,params,policy)
    eval_rs = agent.run(10, False, "manual")


def train_stratified():
    params = {
        "discount_factor": 0.95,
        "epsilon": 0.5,
        "epsilon_decay": 1,
        "min_epsilon": 0.001,
        "learning_rate": 0.1,
        "min_learning_rate": 0.001,
        "learning_rate_decay": 1,
    }

    game_33 = Game((100, 100, 3, 3), True)

    with open('models/model_bottom_up.pickle', 'rb') as f:
        policy = pickle.load(f)

    points_pair = [(3,3),(2,3),(3,2),(2,2),(1,3),(3,1),(1,2),(2,1),(0,3),(3,0),(1,1),(0,2),(2,0),(0,1),(1,0)]
    agent = QLearningAgent(game_33,params,policy)
    for pair in points_pair:
        game = Game((100,100,pair[0],pair[1]),True)
        agent.set_env(game)
        agent.run(500000, True)
    game = Game()
    agent.set_env(game)
    episode_reward, policy = agent.run(1000000, True)

    with open('models/model_bottom_up_2.pickle', 'wb') as f:
        pickle.dump(policy, f, protocol=pickle.HIGHEST_PROTOCOL)

    eval_rs = agent.run(1000, False, "auto")

    with open('models/model_10choice_15m.pickle', 'rb') as f:
        policy_2 = pickle.load(f)
    eval_agent = QLearningAgent(game,params,policy_2)
    eval_rs = agent.run(1000, False, "model", eval_agent)

def test_model():
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
    with open('models/model_bottom_up.pickle', 'rb') as f:
        policy = pickle.load(f)
    agent = QLearningAgent(game,params,policy)

    with open('models/model_bottom_up_2.pickle', 'rb') as f:
        policy_2 = pickle.load(f)
    eval_agent = QLearningAgent(game,params,policy_2)

    # eval_rs = agent.run(10, False, "manual")
    eval_rs = agent.run(1000, False, "model", eval_agent)

if __name__ == "__main__":
    # train_stratified()
    test_model()