import numpy as np
import random
from cmath import sqrt, sin, cos, acos, exp, pi
from Qubit import QubitSystem
from Gates import Gate

class GateApplier:
    def __init__(self, gate: Gate, qubitIndexes):
        self.gate = gate
        self.qubitIndexes = qubitIndexes

class LTS:
    def __init__(self, init: QubitSystem):
        self.initialState = init
        self.P = set()
        self.T = {}
    
    def addTransition(self, p1: QubitSystem, p2: GateApplier):
        self.P.add(p1)
        self.T[p1] = p2
    
    def get(self, p1: QubitSystem):
        return self.T[p1]

