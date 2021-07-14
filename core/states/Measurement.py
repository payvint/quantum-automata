class Measurement:
    def  __init__(self, length, listOfRes, listOfPos):
        self.name = "Measurement"
        self.map = {}
        for i in range(length):
            self.map[listOfRes[i]] = listOfPos[i]
    
    def getPos(self, res):
        return self.map[res]