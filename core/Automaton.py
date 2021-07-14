class Automaton:
    def __init__(self, listOfOps, registry):
        self.listOfOps = listOfOps
        self.registry = registry
        self.route = ""
        self.measurementOutcomes = []

    def operate(self):
        currentPos = 0
        exit = False
        while not exit:
            self.route += str(currentPos)
            if self.listOfOps[currentPos].name == "Exit":
                exit = True
            elif self.listOfOps[currentPos].name == "Measurement":
                # measure list of qubits
                res = self.registry.measure()
                self.measurementOutcomes.append(res)
                newPos = self.listOfOps[currentPos].getPos(res)
                currentPos = newPos
            elif self.listOfOps[currentPos].name == "Gate":
                res = self.registry.applyGate(self.listOfOps[currentPos])
                self.measurementOutcomes.append(res)
                newPos = self.listOfOps[currentPos].getPos()
                currentPos = newPos

    def getMeasurementOutcomes(self):
        return self.measurementOutcomes
    
    def getWord(self):
        return self.route

# Examples:
# QubitCleaner Done
# Teleportation 
# Ternary qubit measurement
# Deutsch-Josza?
# Grover