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

    def measure(self):
        if self.vector[0] > self.vector[1]:
            return np.array([0, 1], dtype=complex)
        elif self.vector[0] < self.vector[1]:
            return np.array([1, 0], dtype=complex)
        randNumber = random.randint(0, 1)
        return np.array([randNumber, (randNumber + 1) % 2], dtype=complex)

    def measureAndSafe(self):
        self.vector = self.measure()

    def apply(self, gate):
        self.vector = gate.calculate(self.vector)
    
    def set(self, x, y):
        self.vector = np.array([x, y], dtype=complex)

class QubitSystem:
    def __init__(self, n):
        self.system = [Qubit()] * n

    def getVector(self):
        totalVector = np.array([], dtype=complex)
        for qubit in self.system:
            np.append(totalVector, qubit.getVector())
        return totalVector
    
    def measure(self):
        totalVector = np.array([], dtype=complex)
        for qubit in self.system:
            np.append(totalVector, qubit.measure())
        return totalVector
    
    def measureAndSafe(self):
        totalVector = np.array([], dtype=complex)
        for qubit in self.system:
            np.append(totalVector, qubit.measureAndSafe())
        return totalVector
    
    def apply(self, gate, qubitsIndexes):
        totalVector = np.array([], dtype=complex)
        for index in qubitsIndexes:
            np.append(totalVector, self.system[index].getVector())
        totalVector = gate.calculate(totalVector)
        for index in qubitsIndexes:
            self.system[index].set(totalVector[index * 2], totalVector[index * 2 + 1])



