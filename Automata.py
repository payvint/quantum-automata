import numpy as np
from typing import List
from math import sqrt

State = (np.ndarray, float, float)


def getComplementaryMatrix(pairOfMatrixes: List[np.ndarray]) -> np.ndarray:
    size = pairOfMatrixes[0].shape[0]
    diag = np.eye(size)
    s = sum(pairOfMatrixes)
    return diag - s

class Automata:
    def __init__(
        self,
        alphabet: str,
        initState: np.ndarray,
        transMatrixes: List[np.ndarray],
        projMeasurements: List[List[np.ndarray]]
    ):
        self.alphabet = alphabet

        self.initState = initState

        for matrix in transMatrixes:
            if not np.allclose(np.eye(matrix.shape[0]), np.conjugate(matrix).T @ matrix):
                raise Exception("Transition matrix %s is not unitary" % matrix)
        self.transMatrixes = transMatrixes

        if len(projMeasurements[0]) == 3:
            # acc, rej and non matrices are provided
            for i, measurement in enumerate(projMeasurements):
                size = measurement[0].shape[0]
                s = sum(measurement)
                if not np.array_equal(s, np.eye(size)):
                    print(s, np.eye(size))
                    raise Exception('Wrong ', i, 'th measurement')
            self.projMeasurements = projMeasurements
        elif len(projMeasurements[0]) == 2:
            # we have to calculate non halting matrix
            self.projMeasurements = [pairOfMatrixes + [getComplementaryMatrix(pairOfMatrixes)] for pairOfMatrixes in projMeasurements]
        else:
            raise Exception("Wrong measurements list")

    def process(self, word: str) -> (float, float):

        commonState = (self.initState, 0, 0)

        for letter in word:
            transMatrix = self.transMatrixes[self.alphabet.index(letter)]
            projMeasurement = self.projMeasurements[self.alphabet.index(letter)]

            commonState = self.processWord(commonState, transMatrix, projMeasurement)

        transMatrix = self.transMatrixes[-1]
        projMeasurement = self.projMeasurements[-1]
        commonState = self.processWord(commonState, transMatrix, projMeasurement)
        final_state, acceptance, rejection = commonState

        error = abs(1 - acceptance - rejection)
        return commonState[1], error

    def processWord(self,
                     commonState: State,
                     transMatrix: np.ndarray,
                     projMeasurement: List[np.ndarray]) -> (State, np.ndarray, np.ndarray):

        projMeasurementAccept = projMeasurement[0]
        projMeasurementReject = projMeasurement[1]
        projMeasurementNon = projMeasurement[2]

        state = commonState[0]

        newState = projMeasurementNon @ transMatrix @ state

        acceptance = commonState[1]
        v = projMeasurementAccept @ transMatrix @ state
        acceptance += np.vdot(v, v)

        rejection = commonState[2]
        v = projMeasurementReject @ transMatrix @ state
        rejection += np.vdot(v, v)

        return newState, acceptance, rejection
