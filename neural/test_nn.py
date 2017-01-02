from network import NeuralNetwork
import numpy as np

nn = NeuralNetwork(3)
for i in range(1000):
    nn.set_input(np.array([1,0,0,0,0,0,0,0,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,0,1,0,0,0,0,0]))

    nn.set_input(np.array([1,0,0,0,0,0,1,0,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,0,0,0,0,-1,0,0]))

nn.set_input(np.array([1,0,0,0,0,0,1,0,0]))
nn.update()
out = nn.get_output()
out = np.negative(out)
out = np.exp(out)
print out / np.sum(out)
