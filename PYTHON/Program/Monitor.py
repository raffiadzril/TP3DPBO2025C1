from OutputDevice import OutputDevice

class Monitor(OutputDevice):
    def __init__(self, refreshRate=0, resolution="", jenisOutput="", outputLatency="", merk="", nama=""):
        super().__init__(jenisOutput, outputLatency, merk, nama)
        self.refreshRate = refreshRate
        self.resolution = resolution

    def setRefreshRate(self, refreshRate):
        self.refreshRate = refreshRate

    def setResolution(self, resolution):
        self.resolution = resolution

    def getRefreshRate(self):
        return self.refreshRate

    def getResolution(self):
        return self.resolution
