import random
from utils import lerp
from config import DATABASE
import dill

class NN:
    def __init__(self, neuronCount):
        self.levels = []
        self.neuronCount = neuronCount
        for i in range(len(neuronCount)-1): # 0 1
            self.levels.append(Level(neuronCount[i], neuronCount[i+1], i)) # 5 6 4    

    def feedForeward(self, givenInputs, network):
        outputs =  network.levels[0].feedForward(givenInputs, network.levels[0]);
        print(outputs)
        for i in range(1, len(network.levels)):
            outputs= network.levels[i].feedForward(outputs,network.levels[i])
        return outputs

    def dump(self, network):
        with open('network.pkl', 'w') as pkl: 
            dill.dump(network, pkl)

class Level:
    def __init__(self,inputCount,outputCount, ind):
        self.inputs =[0 for i in range(inputCount)]
        self.outputs = [0 for i in range(outputCount)]
        self.biases = [0 for i in range(outputCount)]

        self.weights=[];
        for i in range(inputCount):
            self.weights.append([0 for i in range(outputCount)])
        
        for i in range(inputCount):
            for j  in range(outputCount):
                self.weights[i][j]=random.random()

        for i in range(outputCount): #biases
            self.biases[i]=random.random()
    
    def activation_function(self, x):
        return x

    def feedForward(self, givenInputs,level):
        for i in range(len(level.inputs)):
            level.inputs[i]=givenInputs[i]
        for i in range(len(level.outputs)):
            sum = 0
            for j in range(len(level.inputs)):
                sum+=level.inputs[j]*level.weights[j][i]
            level.outputs[i] =self.activation_function(sum - level.biases[i])
        return level.outputs

