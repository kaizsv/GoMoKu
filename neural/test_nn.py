from network import NeuralNetwork
import numpy as np

'''
    A simple test of 3 blocks.

    | - | - | - |

    if all empty than state equal (0,0,0,0,0,0,1,1,1)
    if block 1 fill with black (1,0,0,0,0,0,0,1,1)
    if block 1 fill with white (0,0,0,1,0,0,0,1,1)
    and output an array of 3 element.
'''

nn = NeuralNetwork(3)
for i in range(1000):
    '''
        black win
    '''
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,0,1]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(-1, np.array([1,0,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(-1, np.array([1,0,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(-1, np.array([0,0,1]))

'''
#----------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,1]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))

    nn.set_input(np.array([0,0,1,1,0,0,0,1,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))
#--------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,1]))

    nn.set_input(np.array([0,1,0,0,0,1,1,0,0]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))
#------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,1,0]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,1]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(-1, np.array([1,0,0]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,1,0]))
#------------------------------------------------
    # white win
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,0,1]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(-1, np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,1]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(-1, np.array([1,0,0]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(1, np.array([0,0,1]))
#------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(-1, np.array([1,0,0]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(-1, np.array([0,0,1]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(1, np.array([1,0,0]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(1, np.array([0,1,0]))
'''
nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
nn.update()
out = nn.get_output()
print out
