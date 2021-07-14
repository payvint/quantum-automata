class Gate:
    def __init__(self, gate, applyPos, pos):
        self.name = "Gate"
        self.gateName = gate
        self.pos = pos
        self.applyPos = applyPos

    def getGate(self):
        return self.gateName

    def getPos(self):
        return self.pos
    
    def getApplyPos(self):
        return self.applyPos