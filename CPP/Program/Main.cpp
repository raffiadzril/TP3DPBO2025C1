#include <bits/stdc++.h>
#include "CPU.cpp"
#include "Ram.cpp"
#include "Harddrive.cpp"
#include "Komputer.cpp"
#include "OutputDevice.cpp"
#include "InputDevice.cpp"
#include "Monitor.cpp"
#include "Headset.cpp"



using namespace std;

int main(){

    ios::sync_with_stdio(0); cin.tie();

    CPU cpu1(8, 3.6, "Intel", "Core i7 9700K");
    Ram ram1(16, "DDR4", "Corsair", "Vengeance LPX");
    Ram ram2(16, "DDR4", "Kingston", "HyperX Fury");
    Harddrive harddrive1(1000, "SSD", "Samsung", "EVO 970");
    OutputDevice printer("Hardcopy", "10ms", "Canon", "Pixma");
    InputDevice keyboard("Text", "1ms", "Logitech", "G213");
    InputDevice mouse("Pointing", "1ms", "Logitech", "G102");
    Monitor monitor1(144, "1920x1080", "HDMI", "5ms", "Lenovo", "l24q-10");
    Monitor monitor2(144, "1920x1080", "HDMI", "5ms", "Gigabyte", "G27F");
    Headset headset1(true, 100, "Suara", "10ms", "Voice", "1ms", "Logitech", "G433");

    OutputDevice speaker("Suara", "10ms", "Logitech", "Z313");

    Komputer kompute1("Komputer_Dapis", cpu1, {ram1, ram2}, harddrive1, {printer}, {keyboard, mouse}, {monitor1, monitor2});
    kompute1.addOutputDevice(speaker);
    cout << "Nama Komputer         : " << kompute1.getNama() << endl;
    cout << "Nama CPU              : " << kompute1.getCpu().getNama() << endl;
    cout << "Merk CPU              : " << kompute1.getCpu().getMerk() << endl;
    cout << "Jumlah Core CPU       : " << kompute1.getCpu().getJumlahCore() << endl;
    cout << "Kecepatan CPU         : " << kompute1.getCpu().getKecepatanGHz() << " GHz" << endl;
    cout << "Nama Harddrive        : " << kompute1.getHarddrive().getNama() << endl;
    cout << "Merk Harddrive        : " << kompute1.getHarddrive().getMerk() << endl;
    cout << "Kapasitas Harddrive   : " << kompute1.getHarddrive().getKapasitasGB() << " GB" << endl;
    cout << "Tipe Drive Harddrive  : " << kompute1.getHarddrive().getTipeDrive() << endl;

    cout << "RAM: " << endl;
    int index = 1;
    for (Ram ram : kompute1.getRamList()) {
        cout << "  " << index++ << ". Nama          : " << ram.getNama() << endl;
        cout << "     Merk          : " << ram.getMerk() << endl;
        cout << "     Kapasitas     : " << ram.getKapasitasGB() << " GB" << endl;
        cout << "     DDR           : " << ram.getDdr() << endl;
    }
    
    cout << "Output Device: " << endl;
    index = 1;
    for (OutputDevice outputDevice : kompute1.getOutputDeviceList()) {
        cout << "  " << index++ << ". Nama          : " << outputDevice.getNama() << endl;
        cout << "     Merk          : " << outputDevice.getMerk() << endl;
        cout << "     Jenis Output  : " << outputDevice.getJenisOutput() << endl;
        cout << "     Output Latency: " << outputDevice.getOutputLatency() << endl;
    }

    index = 1;
    cout << "Input Device: " << endl;
    for (InputDevice inputDevice : kompute1.getInputDeviceList()) {
        cout << "  " << index++ << ". Nama          : " << inputDevice.getNama() << endl;
        cout << "     Merk          : " << inputDevice.getMerk() << endl;
        cout << "     Jenis Input   : " << inputDevice.getJenisInput() << endl;
        cout << "     Input Latency : " << inputDevice.getInputLatency() << endl;
    }

    index = 1;
    cout << "Monitor: " << endl;
    for (Monitor monitor : kompute1.getMonitorList()) {
        cout << "  " << index++ << ". Nama          : " << monitor.getNama() << endl;
        cout << "     Merk          : " << monitor.getMerk() << endl;
        cout << "     Refresh Rate  : " << monitor.getRefreshRate() << " Hz" << endl;
        cout << "     Resolution    : " << monitor.getResolution() << endl;
    }

    cout << "Komponen di luar Komputer" << endl;
    // Headset
    cout << "Headset: " << endl;
    cout << "  Nama          : " << headset1.OutputDevice::getNama() << endl;
    cout << "  Merk          : " << headset1.OutputDevice::getMerk() << endl;
    cout << "  Is Wireless   : " << headset1.getIsWireless() << endl;
    cout << "  Sound Level   : " << headset1.getSoundLevelDB() << " dB" << endl;
    cout << "  Jenis Output  : " << headset1.getJenisOutput() << endl;
    cout << "  Output Latency: " << headset1.getOutputLatency() << endl;
    cout << "  Jenis Input   : " << headset1.getJenisInput() << endl;
    cout << "  Input Latency : " << headset1.getInputLatency() << endl;


    return 0;
}