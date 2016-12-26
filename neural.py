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

    def set_input(self, x):
        self.input = x

    def get_output(self):
        return self.output.copy()

    def update(self):
        for i in range(num_hidden_layer):
            w = self.hidden_layers[i]
            inputs = np.dot(w, inputs)
            # TODO: nonlinearlize
        self.output = np.dot(self.output_layer, inputs)

    def forward(self, inputs):
        self.set_input(inputs)
        self.update()

    def backward(self, action_gold):
        self.set_input(action_gold)
        self.update()
        
        # TODO: (1.0 - out) * out
        # calculate output characteristic
        out = self.get_output()
        out_error = np.subtract(action_gold, out)

        for i in reversed(range(num_hidden_layer)):
            pass
            

nn = NeuralNetwork()
#print nn.forward(np.array([1,1,1,1,1,1,1,1,1]))
