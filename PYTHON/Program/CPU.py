from Komponen import Komponen

class CPU(Komponen):
    def __init__(self, jumlahCore=0, kecepatanGhz=0.0, merk="", nama=""):
        super().__init__(merk, nama)
        self.jumlahCore = jumlahCore
        self.kecepatanGhz = kecepatanGhz

    def setJumlahCore(self, jumlahCore):
        self.jumlahCore = jumlahCore

    def setKecepatanGhz(self, kecepatanGhz):
        self.kecepatanGhz = kecepatanGhz

    def getJumlahCore(self):
        return self.jumlahCore

    def getKecepatanGhz(self):
        return self.kecepatanGhz
