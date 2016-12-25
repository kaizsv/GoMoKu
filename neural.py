import numpy as np

num_hidden_layer = 1

class NeuralNetwork(object):
    def __init__(self, input_size, hidden_size, output_size):
        # input and output
        self.input = None
        self.output = None
        # weights of layers
        self.hidden_layers = [np.ones(hidden_size, input_size)]
        for i in range(1, num_hidden_layer):
            self.hidden_layers.append(np.ones(hidden_size, hidden_size))
        self.output_layer = np.ones(output_size, hidden_size)

    def set_input(self, X):
        self.input = X

    def get_output(self):
        return self.output
