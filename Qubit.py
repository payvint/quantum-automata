import numpy as np
import random
from cmath import sqrt, sin, cos, arccos exp, pi

# define qubit in standart base of Bloch sphere
class Qubit:
    def __init__(self, *args):
        angleTetha = random.uniform(0.0, 2 * pi)
        anglePhi = random.uniform(0.0, 2 * pi)
        if len(args) == 2:
            angleTetha = pi / 180.0 * args[0]
            anglePhi = pi / 180.0 * args[1]
        elif len(args) != 0:
            raise "Qubit initialization error"
        self.vector = np.array([cos(angleTetha / 2.0), exp(1j * anglePhi) * sin(angleTetha / 2.0)], dtype=complex)
    
    def getVector(self):
        return self.vector

    def measure(self):
        angleTetha = arccos(self.vector[0]) * 2
        return np.array([angleTetha / pi, (pi - angleTetha) / pi], dtype=complex)

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
    
    def apply(self, gate, qubitsIndexes):
        totalVector = np.array([], dtype=complex)
        for index in qubitsIndexes:
            np.append(totalVector, self.system[index].getVector())
        totalVector = gate.calculate(totalVector)
        for index in qubitsIndexes:
            self.system[index].set(totalVector[index * 2], totalVector[index * 2 + 1])



