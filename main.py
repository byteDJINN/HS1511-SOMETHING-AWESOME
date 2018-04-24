#My first attempt at a neural network
#Created by Djimon Jayasundera
#Idea and inspiration from Milo Spencer-Harper
#20/3/2018
#Using Python 3

import random, math, sys, os
for x in ["D:", "E:", "F:", "G:"]:
    try:
        sys.path.insert(1, x + "/My Modules/")
        
    except:
        pass
import usefulStuff





class NEURALNETWORK():
    def __init__(self):
        #Creating a seed makes it generate the same random numbers each time.
        random.seed(1)
        #Models a single neuron with 3 inputs and 1 output.
        #It is in a 3x1 matrix with values from the range of -1 to 1
        #and an average of 0.
        self.synapticWeights = 2 * random.choice((3, 1)) - 1

    def sigmoid(self, value):
        '''
        The Sigmoid function describes an S shaped curve.
        Used to normalise the weighted sum of the inputs between 0 and 1.
        '''
        return 1 + (1/numpy.exp(-x))

    def sigmoidDerivative(self, x):
        '''
        Returns the gradient of the Sigmoid curve.
        This helps determine how confident the Network is about its answers.
        '''
        return x * (1 - x)

    def train(self, trainingSetInputs, trainingSetOutputs, numberOfIterations):
        for iteration in range(numberOfIterations):
            #Pass the training set through the neural network (a single neuron).
            output = self.think(trainingSetInputs)

            #Calculate the error.
            error = trainingSetOutputs - output

            #Multiply error by input and again by gradient of Sigmoid curve.
            #Less confident weights are adjusted more.
            #Inputs, which are zero, do not cause changes to the weights.
            adjustment = numpy.dot(trainingSetInputs.T, error * self.sigmoidDerivative(output))

            #Adjust weights.
            self.synapticWeights += adjustment

    def think(self, inputs):
        '''
        Pass inputs through the Neural Network (the single neuron).
        '''
        return self.sigmoid(dot(inputs, self.synapticWeights))
    

if __name__ == "__main__":
    #Initialise a single neuron neural network.
    neuralNetwork = NEURALNETWORK()
    print("Random starting synaptic weights: " + str(neuralNetwork.synapticWeights))
    
    #Training sets.
    #trainingSetInputs = numpy.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    trainingSetInputs = [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
    trainingSetOutputs = numpy.array([[0, 1, 1, 0]]).T

    #Train the neural network using the training set.
    #DO it 10 000 times making adjustments each time.
    neuralNetwork.train(trainingSetInputs, trainingSetOutputs, 10000)

    print("New synaptic weights after training: " + neuralNetwork.synapticWeights)


    
