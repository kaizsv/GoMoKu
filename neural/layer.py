import numpy as np

class NeuralLayer(object):

    def __init__(self, size, in_size):
        self.size = size
        self.in_size = in_size
        self.w = np.random.rand(size, in_size) / (size + in_size)
        self.output = None

    def modify_weight(self, delta):
        delta = delta.reshape(len(delta), 1)
        self.w += delta

    def get_weight(self):
        return self.w.copy()

    def get_output(self):
        return self.output.copy()

    def update(self, x):
        self.output = np.dot(self.w, x)
        self._set_non_linear_out()

    def _set_non_linear_out(self):
        self.output = np.tanh(self.output)

    def get_non_linear_derivative_out(self):
        return (1.0 - np.square(np.tanh(self.output)))
