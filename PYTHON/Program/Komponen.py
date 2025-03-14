class Komponen:
    def __init__(self, merk="", nama=""):
        self._merk = merk
        self._nama = nama

    def setMerk(self, merk):
        self._merk = merk

    def setNama(self, nama):
        self._nama = nama

    def getMerk(self):
        return self._merk

    def getNama(self):
        return self._nama
