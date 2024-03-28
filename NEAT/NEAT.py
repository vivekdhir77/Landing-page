import FF
import random
import NN
from utils import lerp

class NEAT:
    def __init__(self,  NetworkArchitecture, population=100):
        self.population_size = 10
        self.NetworkArchitecture =  NetworkArchitecture
        self.population = [NN(self.NetworkArchitecture) for _ in range(self.population_size)]

    def fitness(self):
        pass

    def mutate(self, network, amount = 1): # amount is in percentage
        for level in range(len(network.levels)):
            for i in range(len(level.biases)):
                network.levels[level].biases[i]=lerp(network.levels[level].biases[i], random.random()*2-1,amount)
            for i in range(len(level.weights)):
                for j in range(len(level.weights[i])):
                    network.levels[level].weights[i][j]=lerp(network.levels[level].weights[i][j],random.random()*2-1,amount)

    def crossover(self, network1, network2, probability=0.5): # coded this with the assumption that both networks have same architecture
        NewNetwork = network1 
        for level in range(len(NewNetwork.levels)):
            for i in range(len(level.biases)):
                if(random.random()>probability):
                    NewNetwork.levels[level].biases[i]=network1.levels[level].biases[i]
                else:
                    NewNetwork.levels[level].biases[i]=network2.levels[level].biases[i]
            for i in range(len(level.weights)):
                for j in range(len(level.weights[i])):
                    if(random.random()>probability):
                        NewNetwork.levels[level].weights[i][j]=network1.levels[level].weights[i][j]
                    else:
                        NewNetwork.levels[level].weights[i][j]=network2.levels[level].weights[i][j]
        pass

    def run(self):
        pass
