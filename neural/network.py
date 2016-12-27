from layer import NeuralLayer
import numpy as np

input_size = 9
output_size = 9
layer_size = [input_size, 50]
num_hidden_layer = len(layer_size) - 1

class NeuralNetwork(object):
    def __init__(self):
        # input
        self.input = None
        # weights of layers
        self.hidden_layers = list()
        for i in range(num_hidden_layer):
            layer = NeuralLayer(layer_size[i+1], layer_size[i])
            self.hidden_layers.append(layer)
        self.output_layer = NeuralLayer(output_size, layer_size[-1])

    def set_input(self, x):
        self.input = x

    def get_input(self):
        return self.input.copy()

    def get_output(self):
        return self.output_layer.get_output()

    def update(self):
        x = self.input
        for i in range(num_hidden_layer):
            self.hidden_layers[i].update(x)
            x = self.hidden_layers[i].get_output()
        self.output_layer.update(x)

    def forward(self, inputs):
        self.set_input(inputs)
        self.update()
        return self.get_oddutput()

    def backward(self, action_gold):
        self.set_input(action_gold)
        self.update()

        # calculate output error
        out = self.get_output()
        characteristic = np.subtract(action_gold, out)
        out_error = map(lambda x, y, z: x * y * z, characteristic, 1.0-out, out)
        out_error = np.array(out_error)

        # hidden layers error
        hidden_errors = list()
        higher_error = out_error
        for i in reversed(range(num_hidden_layer)):
            w = self.hidden_layers[i].get_weight()
            error = np.dot(w, higher_error)
            hidden_errors.append(error.copy())
            higher_error = error
        hidden_errors.reverse()

        # modify hidden layers weights
        for i in range(num_hidden_layer):
            hidden_layer = self.hidden_layers[i]
            w = hidden_layer.get_weight()
            delta = np.dot(hidden_errors[i].T, hidden_layer.get_non_linear_der_out())
            hidden_layer.modify_weight(delta)

        # modify output layer weight
        w = self.output_layer.get_weight()
        delta = np.dot(out_error.T, self.output_layer.get_non_linear_der_out())
        self.output_layer.modify_weight(delta)

