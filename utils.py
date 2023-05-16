import matplotlib.pyplot as plt
import numpy as np

def plot_reward(episode_rewards):
    total_episode = len(episode_rewards)
    index = 1000*(np.arange(total_episode/1000)+1)
    mean_episode = []
    for i in range(int(total_episode/1000)):
        tmp = episode_rewards[i*1000:(i+1)*1000]
        mean_episode.append(sum(tmp)/len(tmp))
    plt.plot(index, mean_episode)
    plt.ylabel("reward")
    plt.xlabel("episode")
    plt.title("training reward")
    plt.show()