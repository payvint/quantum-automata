import numpy as np
import random
from cmath import sqrt, sin, cos, exp, pi

class Gate:
    def __init__(self, tensor):
        self.tensor = tensor

    def __mul__(self, other):
        return np.tensordot(self.tensor, othe.tensor, 0)

    def calculate(self, vector):
        return np.dot(self.tensor, vector)

class I(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0],
                [0, 1]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class X(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [0, 1],
                [1, 0]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class Y(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [0, -1j],
                [1j, 0]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class Z(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0],
                [0, -1]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class H(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 1],
                [1, -1]
            ],
            dtype=complex
        ) * (1.0 / sqrt(2.0))
        super.__init__(tensor)

class P(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0],
                [0, 1j]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class T(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0],
                [0, exp((1j * pi) / 4.0)]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class CNOT(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class CZ(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, -1]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class SWAP(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1]
            ],
            dtype=complex
        )
        super().__init__(tensor)

class CCNOT(Gate):
    def __init__(self):
        tensor = np.array(
            [
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0]
            ],
            dtype=complex
        )
        super().__init__(tensor)