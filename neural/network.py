from layer import NeuralLayer
import numpy as np

class NeuralNetwork(object):
    def __init__(self, size, phase=3):
        # layer parameters
        self.input_size = phase * size ** 2
        self.output_size = size ** 2
        self.layer_size = [self.input_size, 162, 27]
        self.num_hidden_layer = len(self.layer_size) - 1
        # learning rate
        self.eta = 0.01
        # input
        self.input = None
        # weights of layers
        self.hidden_layers = list()
        for i in range(self.num_hidden_layer):
            layer = NeuralLayer(self.layer_size[i+1], self.layer_size[i])
            self.hidden_layers.append(layer)
        self.output_layer = NeuralLayer(self.output_size, self.layer_size[-1])

    def __str__(self):
        s_layer = '_'.join(map(str, self.layer_size)) + '_' + str(self.output_size)
        return 'nn_' + s_layer

    def set_input(self, x):
        self.input = x

    def get_input(self):
        return self.input.copy()

    def get_output(self):
        return self.output_layer.get_output()

    def update(self):
        x = self.get_input()
        for i in range(self.num_hidden_layer):
            self.hidden_layers[i].update(x)
            x = self.hidden_layers[i].get_output()
        self.output_layer.update(x)

    def backpropagation(self, reward, action_gold):
        # calculate output error
        out = self.get_output()
        characteristic = np.subtract(action_gold, out)
        out_error = reward * characteristic * self.output_layer.get_d_non_linear_out()

        # hidden layers error
        hidden_errors = list()
        pre_layer = self.output_layer
        pre_error = out_error
        for i in reversed(range(self.num_hidden_layer)):
            h_layer_out = self.hidden_layers[i].get_d_non_linear_out()
            w = pre_layer.get_weight()
            error = np.dot(pre_error, w)
            error = error * h_layer_out
            hidden_errors.append(error.copy())
            pre_layer = self.hidden_layers[i]
            pre_error = error.copy()
        hidden_errors.reverse()

        # modify hidden layers weights
        for i in range(self.num_hidden_layer):
            hidden_layer = self.hidden_layers[i]
            hidden_input = hidden_layer.get_input()
            delta = self.eta * np.outer(hidden_errors[i], hidden_input)
            hidden_layer.modify_weight(delta)

        # modify output layer weight
        out_input = self.output_layer.get_input()
        delta = self.eta * np.outer(out_error, out_input)
        self.output_layer.modify_weight(delta)
