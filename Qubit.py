import numpy as np
import random
from cmath import sqrt, sin, cos, acos, exp, pi

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

    def measureProbability(self):
        angleTetha = acos(self.vector[0]) * 2.0
        return np.array([angleTetha / pi, (pi - angleTetha) / pi], dtype=complex)
    
    def measure(self):
        vector = self.measureProbability()
        if vector[0] >= vector[1]:
            return np.array([0.0, 1.0], dtype=complex)
        else:
            return np.array([1.0, 0.0], dtype=complex)

    def apply(self, gate):
        self.vector = gate.calculate(self.vector)
    
    def set(self, x, y):
        self.vector = np.array([x, y], dtype=complex)

class QubitSystem:
    def __init__(self, *args):
        if len(args) == 1:
            self.system = [Qubit()] * args[0]
        elif len(args) == 2:
            system = []
            for qubit in args[1]:
                system.append(Qubit(qubit[0], qubit[1]))
            self.system = system
        else:
            raise "Qubit system initialization error"

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

    def measureProbability(self):
        totalVector = np.array([], dtype=complex)
        for qubit in self.system:
            np.append(totalVector, qubit.measureProbability())
        return totalVector
    
    def apply(self, gate, qubitsIndexes):
        totalVector = np.array([], dtype=complex)
        for index in qubitsIndexes:
            np.append(totalVector, self.system[index].getVector())
        totalVector = gate.calculate(totalVector)
        for index in qubitsIndexes:
            self.system[index].set(totalVector[index * 2], totalVector[index * 2 + 1])

    def getSize(self):
        return 2 ** len(self.system)



