import numpy as np
import random
from cmath import sqrt, sin, cos, acos, exp, pi
from Qubit import QubitSystem
from LTS import LTS
from queue import Queue

class Matrix:
    def __init__(self, init: QubitSystem, lts: LTS):
        self.initialState = init
        self.lts = lts
        self.matrix = [[] * self.initialState.getSize()] * self.initialState.getSize()
    
    def build(self):
        allQubitSystems = list(self.lts.P)
        for qubitSystem in allQubitSystems:
            gateApp = self.lts.get(qubitSystem)
            appliedQubitSystem = qubitSystem.apply(gateApp.gate, gateApp.qubitIndexes)
            self.matrix[qubitSystem][appliedQubitSystem] = gateApp