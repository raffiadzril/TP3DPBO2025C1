from Komponen import Komponen

class InputDevice(Komponen):
    def __init__(self, jenisInput='', inputLatency='', merk='', nama=''):
        super().__init__(merk, nama)
        self.jenisInput = jenisInput
        self.inputLatency = inputLatency

    def setJenisInput(self, jenisInput):
        self.jenisInput = jenisInput

    def setInputLatency(self, inputLatency):
        self.inputLatency = inputLatency

    def getJenisInput(self):
        return self.jenisInput

    def getInputLatency(self):
        return self.inputLatency
