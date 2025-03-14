from OutputDevice import OutputDevice
from InputDevice import InputDevice

class Headset(OutputDevice, InputDevice):
    def __init__(self, isWireless=False, soundLevelDB=0, jenisOutput="", outputLatency="", jenisInput="", inputLatency="", merk="", nama=""):
        OutputDevice.__init__(self, jenisOutput, outputLatency, merk, nama)
        InputDevice.__init__(self, jenisInput, inputLatency, merk, nama)
        self.isWireless = isWireless
        self.soundLevelDB = soundLevelDB

    def setIsWireless(self, isWireless):
        self.isWireless = isWireless

    def setSoundLevelDB(self, soundLevelDB):
        self.soundLevelDB = soundLevelDB

    def getIsWireless(self):
        return self.isWireless

    def getSoundLevelDB(self):
        return self.soundLevelDB
