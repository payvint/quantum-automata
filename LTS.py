import numpy as np
import random
from cmath import sqrt, sin, cos, acos, exp, pi
from Qubit import QubitSystem

class LTS:
    def __init__(self, init: QubitSystem):
        self.initialState = init
        self.P = set()
        self.T = {}
    
    def addTransition(self, p1: QubitSystem, p2: QubitSystem):
        self.P.add(p1)
        self.P.add(p2)
        self.T[p1] = p2
    
    def get(self, p1: QubitSystem):
        return self.T[p1]

