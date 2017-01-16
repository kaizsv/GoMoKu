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
for i in range(5000):
    if i % 1000 == 0:
        print i
    '''
        black win
    '''

    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([1,0,0]))
'''
    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([1,0,0,0,0,1,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

#----------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,1]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([0,0,1,1,0,0,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([0,0,1,1,0,0,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,0,1,1,0,0,0,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

#--------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))

    nn.set_input(np.array([0,1,0,0,0,1,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([1,0,0]))

    nn.set_input(np.array([0,1,0,0,0,1,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))

    nn.set_input(np.array([0,1,0,0,0,1,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))
#------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,0,0,0,1,0,1,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,1]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,1,0,1,0,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))
#------------------------------------------------
    # white win
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,0,0,1,1,1,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))

    nn.set_input(np.array([0,0,1,0,1,0,1,0,0]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))
#------------------------------------------------
    nn.set_input(np.array([0,0,0,0,0,0,1,1,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(np.array([0,1,0]))

    nn.set_input(np.array([0,0,0,1,0,0,0,1,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,0,-1]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([-1,0,0]))

    nn.set_input(np.array([1,0,0,0,1,0,0,0,1]))
    nn.update()
    nn.backpropagation(np.array([0,-1,0]))
'''
a=np.array([0,0,0,1,0,0,0,1,1])
nn.set_input(a)
nn.update()
out = nn.get_output()
print a, out
b=np.array([0,1,0,0,0,1,1,0,0])
nn.set_input(np.array([0,1,0,0,0,1,1,0,0]))
nn.update()
print b, nn.get_output()
