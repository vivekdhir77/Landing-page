import os
import pickle

import numpy as np
import gymnasium as gym

runs_per_net = 2

def run():
    population_size = 10
    net = NEAT([2,2,1], population)
    fitnesses = []
    envs = [gym.make("CartPole-v1") for _ in range(population_size)]
    observations = [env[i].reset()[0] for i in range(population_size)]

    for runs in range(runs_per_net):
        terminated = [False for i in range(population_size)]
        while False in terminated: # observation, reward, terminated, truncated, info
            actions = [net.population[i].feedForeward(observation[i], net.population[i]) for i in range(population_size)]
            rewards = [env.step(actions[i]) if terminated[i]==False else 0 for i in range(population_size)]
            net.run(rewards)
    with open('winner', 'wb') as f:
        pickle.dump(net.population[0], f)



if __name__ == '__main__':
    run()