import numpy as np
import random
from cmath import sqrt, sin, cos, exp, pi

# define qubit in standart base
class Qubit:
    def __init__(self):
        angle = random.uniform(0.0, pi / 2.0)
        self.vector = np.array([cos(angle), sin(angle)], dtype=complex)
    
    def getVector(self):
        return self.vector

class QubitSystem:
    def __init__(self, n):
        self.system = [Qubit()] * n

    def getVector(self):
        totalVector = np.array([], dtype=complex)
        for qubit in self.system:
            np.append(totalVector, qubit.getVector())
        return totalVector