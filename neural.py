import numpy as np

input_size = 9
output_size = 9
layer_size = [input_size, 50]
num_hidden_layer = len(layer_size) - 1

class NeuralNetwork(object):
    def __init__(self):
        # input and output
        self.input = None
        self.output = None
        # weights of layers
        self.hidden_layers = list()
        self.output_layer = list()
        self._init_network()

    def _init_network(self):
        for i in range(num_hidden_layer):
            w = np.ones((layer_size[i+1], layer_size[i]))
            self.hidden_layers.append(w.copy())
        self.output_layer = np.ones((output_size, layer_size[-1]))

    def set_input(self, X):
        self.input = X

    def get_output(self):
        return self.output

    def forward(self, inputs):
        for i in range(num_hidden_layer):
            w = self.hidden_layers[i]
            inputs = np.dot(w, inputs)
            # TODO: nonlinearlize
        output = np.dot(self.output_layer, inputs)
        return output

    def backward(self):
        pass

nn = NeuralNetwork()
#print nn.forward(np.array([1,1,1,1,1,1,1,1,1]))
