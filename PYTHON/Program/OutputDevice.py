from Komponen import Komponen

class OutputDevice(Komponen):
    def __init__(self, jenisOutput="", outputLatency="", merk="", nama=""):
        super().__init__(merk, nama)
        self.jenisOutput = jenisOutput
        self.outputLatency = outputLatency

    def setJenisOutput(self, jenisOutput):
        self.jenisOutput = jenisOutput

    def setOutputLatency(self, outputLatency):
        self.outputLatency = outputLatency

    def getJenisOutput(self):
        return self.jenisOutput

    def getOutputLatency(self):
        return self.outputLatency
