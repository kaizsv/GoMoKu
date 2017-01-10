import numpy as np

class NeuralLayer(object):

    def __init__(self, size, in_size):
        self.size = size
        self.in_size = in_size
        self.w = (np.random.rand(size, in_size)-0.5) * np.sqrt(2.0/in_size)
        self.input = None
        self.output = None

    def modify_weight(self, delta):
        self.w += delta

    def get_weight(self):
        return self.w.copy()

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output.copy()

    def update(self, x):
        self.input = x.copy()
        self.output = np.dot(self.w, x)
        self._set_non_linear_out()

    def _set_non_linear_out(self):
        #self.output = self.output * (self.output > 0)
        self.output = np.tanh(self.output)

    def get_d_non_linear_out(self):
        #return 1.0 * (self.output != 0.0)
        return 1.0 - np.square(self.output)
