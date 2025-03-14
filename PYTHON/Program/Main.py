from CPU import CPU
from Ram import Ram
from Harddrive import Harddrive
from Komputer import Komputer
from OutputDevice import OutputDevice
from InputDevice import InputDevice
from Monitor import Monitor
from Headset import Headset

def main():
    cpu1 = CPU(8, 3.6, "Intel", "Core i7 9700K")
    ram1 = Ram(16, "DDR4", "Corsair", "Vengeance LPX")
    ram2 = Ram(16, "DDR4", "Kingston", "HyperX Fury")
    harddrive1 = Harddrive(1000, "SSD", "Samsung", "EVO 970")
    printer = OutputDevice("HardCopy", "10ms", "Canon", "Pixma")
    keyboard = InputDevice("Text", "1ms", "Logitech", "G213")
    mouse = InputDevice("Pointing", "1ms", "Logitech", "G102")
    monitor1 = Monitor(144, "1920x1080", "HDMI", "5ms", "Lenovo", "l24q-10")
    monitor2 = Monitor(144, "1920x1080", "HDMI", "5ms", "Gigabyte", "G27F")
    headset1 = Headset(True, 100, "Suara", "10ms", "Voice", "1ms", "Logitech", "G433")
    speaker = OutputDevice("Suara", "10ms", "Logitech", "Z313")

    komputer1 = Komputer("Komputer_Dapis", cpu1, [ram1, ram2], harddrive1, [printer], [keyboard, mouse], [monitor1, monitor2])
    komputer1.addOutputDevice(speaker)

    print("Nama Komputer    : ", komputer1.getNama())
    print("Nama CPU         : ", komputer1.getCpu().getNama())
    print("Merk CPU         : ", komputer1.getCpu().getMerk())
    print("Jumlah Core CPU  : ", komputer1.getCpu().getJumlahCore())
    print("Kecepatan CPU    : ", komputer1.getCpu().getKecepatanGhz())
    print("Nama Harddrive   : ", komputer1.getHarddrive().getNama())
    print("Merk Harddrive   : ", komputer1.getHarddrive().getMerk())
    print("Kapasitas Harddrive: ", komputer1.getHarddrive().getKapasitasGB())
    print("Tipe Harddrive   : ", komputer1.getHarddrive().getTipeDrive())
    
    print("RAM")
    for i, ram in enumerate(komputer1.getRamList(), start=1):
        print(f"   {i}. Nama         : {ram.getNama()}")
        print(f"      Merk         : {ram.getMerk()}")
        print(f"      Kapasitas    : {ram.getKapasitasGB()}")
        print(f"      DDR          : {ram.getDdr()}")
    
    print("Output Device")
    for i, outputDevice in enumerate(komputer1.getOutputDeviceList(), start=1):
        print(f"   {i}. Nama         : {outputDevice.getNama()}")
        print(f"      Merk         : {outputDevice.getMerk()}")
        print(f"      Jenis        : {outputDevice.getJenisOutput()}")
        print(f"      Latency      : {outputDevice.getOutputLatency()}")

    print("Input Device     : ")
    for i, inputDevice in enumerate(komputer1.getInputDeviceList(), start=1):
        print(f"   {i}. Nama         : {inputDevice.getNama()}")
        print(f"      Merk         : {inputDevice.getMerk()}")
        print(f"      Jenis        : {inputDevice.getJenisInput()}")
        print(f"      Latency      : {inputDevice.getInputLatency()}")
    
    print("Monitor")
    for i, monitor in enumerate(komputer1.getMonitorList(), start=1):
        print(f"   {i}. Nama         : {monitor.getNama()}")
        print(f"      Merk         : {monitor.getMerk()}")
        print(f"      Resolusi     : {monitor.getResolution()}")
        print(f"      Refresh Rate : {monitor.getRefreshRate()}")

    print("\nKomponen di luar komputer")
    print("Headset")
    print("Nama             : ", headset1.getNama())
    print("Merk             : ", headset1.getMerk())
    print("isWireless       : ", headset1.getIsWireless())
    print("Sound Level DB   : ", headset1.getSoundLevelDB())
    print("Jenis Output     : ", headset1.getJenisOutput())
    print("Output Latency   : ", headset1.getOutputLatency())
    print("Jenis Input      : ", headset1.getJenisInput())
    print("Input Latency    : ", headset1.getInputLatency())
    
if __name__ == "__main__":
    main()
