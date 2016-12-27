import numpy as np

class NeuralLayer(object):

    def __init__(self, size, in_size):
        self.size = size
        self.in_size = in_size
        self.w = np.ones((size, in_size))
        self.output = None

    def get_weight(self):
        return self.w.copy()

    def get_output(self):
        return self.output.copy()

    def update(self, x):
        self.output = np.dot(self.w, x)
