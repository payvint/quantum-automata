from Automata import Automata
import numpy as np
import random
from cmath import sqrt, sin, cos, acos, exp, pi


alphabet = 'a'

a_matrix = np.array([[1/2,         1/2,        sqrt(1/2),  0],
                        [sqrt(1 / 2), -sqrt(1/2), 0,          0],
                        [1/2,         1/2,        -sqrt(1/2), 0],
                        [0,           0,          0,          1]])

end_matrix = np.array([[0, 0, 0, 1],
                        [0, 0, 1, 0],
                        [1, 0, 0, 0],
                        [0, 1, 0, 0]])

initState = np.array([[1], [0], [0], [0]])

measurement_acc = np.array([[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 0]])

measurement_rej = np.array([[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 1]])

measurements = [[measurement_acc, measurement_rej], [measurement_acc, measurement_rej]]

gqfa = Automata(alphabet, initState, [a_matrix, end_matrix], measurements)

print('Automata example:')
res = gqfa.process('a')
print('a\t', res)
res = gqfa.process('aa')
print('aa\t', res)

# example from wikipedia: (https://en.wikipedia.org/wiki/Quantum_finite_automata#Measure-once_automata)

# alphabet = '01'
# zero_matrix = np.array([[0, 1], [1, 0]])
# one_matrix = np.array([[1, 0], [0, 1]])
# projection_matrix = np.array([[1, 0], [0, 0]])

# initState = np.array([[1], [0]])

# qfa2 = Automata(alphabet, initState, [zero_matrix, one_matrix], projection_matrix)

# print('Simple automata')
# print('111\t', qfa2.process('111'))
# print('101\t', qfa2.process('101'))
# print('001\t', qfa2.process('001'))
# print('\t', qfa2.process(''))
