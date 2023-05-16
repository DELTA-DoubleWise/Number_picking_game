import numpy as np
import math

def game(env, player=1):
    round = env.scores[0]+env.scores[1]+1
    if round == 1:
        return get_action1()
    elif round == 2:
        return get_action2(env, player)
    elif round == 3:
        return get_action3(env, player)
    elif round == 4:
        return get_action4(env, player)
    elif round == 5:
        return get_action5(env, player)
    elif round == 6:
        return get_action6(env, player)
    elif round == 7:
        return get_action7(env, player)

def check_mustwin(round, env, player):
    t0 = env.points[player]/(7-round)
    t1 = env.points[1-player]-(3-env.scores[1-player])*(env.points[player]/(7-round)+1)
    if t0>=t1:
        x=math.floor(env.points[player]/(7-round))+1
        return True, x
    else:
        return False,0

def get_action1(prob=0.6):
    if np.random.random()<prob:
        return abs(int(np.random.normal(4,2)))
    else:
        return abs(int(np.random.normal(21,5)))

def get_action2(env, player, prob=0.3):
    if env.points[player]>95:
        if np.random.random()<prob:
            action =  abs(int(np.random.normal(3,2)))
        else:
            action = abs(int(np.random.normal(22,8)))
    else:
        if env.scores[1-player]==1:
            action = abs(int(np.random.normal(5,3)))
        else:
            action = abs(int(np.random.normal(9,6)))
    must_win, must_win_strat = check_mustwin(1, env, player)
    if must_win:
        action = must_win_strat
    if action > env.points[player]:
        action = math.floor(np.random.random() * env.points[player])
    return action


def get_action3(env, player, prob1=0.85, prob2=0.5):
    if env.scores[player]==2:
        if np.random.random() < prob1:
            action = abs(int(np.random.normal(8,4)))
        else:
            action = abs(int(np.random.normal(20,5)))
    elif env.scores[player]==1:
        if np.random.random() < prob2:
            action = abs(int(np.random.normal(3,2)))
        else:
            action = abs(int(np.random.normal(20,8)))
    else:
        action = abs(int(np.random.normal(21,6)))
    must_win, must_win_strat = check_mustwin(2, env, player)
    if must_win:
        action = must_win_strat
    if action > env.points[player]:
        action = math.floor(np.random.random() * env.points[player])
    return action

def get_action4(env,player, prob1=0.3, prob2=0.7):
    if env.scores[player]==3:
        action =  abs(int(np.random.normal(5,3)))
    elif env.scores[player]==2:
        if np.random.random() < prob1:
            action = abs(int(np.random.normal(2,1)))
        else:
            action = abs(int(np.random.normal(23,8)))
    elif env.scores[player]==1:
        if np.random.random() < prob2:
            action = abs(int(np.random.normal(10,3)))
        else:
            action = abs(int(np.random.normal(23,6)))
    else:
        action = env.points[1-player]+1
    must_win, must_win_strat = check_mustwin(3, env, player)
    if must_win:
        action = must_win_strat
    if action > env.points[player]:
        action = math.floor(np.random.random() * env.points[player])
    return action


def get_action5(env, player, prob1_1=0.1, prob1_2=0.7, prob2=0.3):
    if env.scores[player]==3:
        rd = np.random.random()
        if rd < prob1_1:
            action = env.points[player]
        elif rd < prob1_2:
            action =  abs(int(np.random.normal(2,1)))
        else:
            action = abs(int(np.random.normal(10,5)))
    elif env.scores[player]==2:
        if env.points[1-player]*2 - env.points[player]<10:
            action =  abs(int(np.random.normal(2,1)))
        else:
            action = abs(int(np.random.normal(23,8)))
    else:
        if np.random.random() < prob2:
            action = abs(int(np.random.normal(9,4)))
        else:
            action = env.points[1 - player] + 1
    must_win, must_win_strat = check_mustwin(4, env, player)
    if must_win:
        action = must_win_strat
    if action > env.points[player]:
        action = math.floor(np.random.random() * env.points[player])
    return action


def get_action6(env, player, prob1=0.5, prob2=0.2):
    if env.scores[player] == 3:
        if np.random.random() < prob1:
            action = math.floor(np.random.random() * 2 + env.points[player] - 5)
        else:
            action = abs(int(np.random.normal(2,1)))
    else:
        if np.random.random() < prob2:
            action = abs(int(np.random.normal(5,2)))
        else:
            action = env.points[1 - player] + 1
    must_win, must_win_strat = check_mustwin(5, env, player)
    if must_win:
        action = must_win_strat
    if action > env.points[player]:
        action = math.floor(np.random.random() * env.points[player])
    return action

def get_action7(env, player):
    return env.points[player]