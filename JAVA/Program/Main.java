package Program;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        CPU cpu1 = new CPU(8, 3.6f, "Intel", "Core i7-9700K");
        Ram ram1 = new Ram(16, "DDR4", "Corsair", "Vengeance LPX");
        Ram ram2 = new Ram(16, "DDR4", "Kingston", "HyperX Fury");
        Harddrive harddrive1 = new Harddrive(1000, "SSD", "Samsung", "EVO 970");
        OutputDevice printer = new OutputDevice("Hardcopy", "10ms", "Canon", "Pixma");
        InputDevice keyboard = new InputDevice("Text", "1ms", "Logitech", "G213");
        InputDevice mouse = new InputDevice("Pointing", "1ms", "Logitech", "G102");
        Monitor monitor1 = new Monitor(144, "1920x1080", "HDMI", "5ms", "Lenovo", "l24q-10");
        Monitor monitor2 = new Monitor(144, "1920x1080", "HDMI", "5ms", "Gigabyte", "G27F");
        Headset headset1 = new Headset(true, 100, "Suara", "10ms", "Logitech", "G433");

        OutputDevice speaker = new OutputDevice("Suara", "10ms", "Logitech", "Z313");

        List<Ram> ramList = new ArrayList<>();
        ramList.add(ram1);
        ramList.add(ram2);

        List<OutputDevice> outputDeviceList = new ArrayList<>();
        outputDeviceList.add(printer);

        List<InputDevice> inputDeviceList = new ArrayList<>();
        inputDeviceList.add(keyboard);
        inputDeviceList.add(mouse);

        List<Monitor> monitorList = new ArrayList<>();
        monitorList.add(monitor1);
        monitorList.add(monitor2);

        Komputer komputer1 = new Komputer("Komputer_Dapis", cpu1, ramList, harddrive1, outputDeviceList, inputDeviceList, monitorList);
        komputer1.addOutputDevice(speaker);

        System.out.println("Nama Komputer         : " + komputer1.getNama());
        System.out.println("Nama CPU              : " + komputer1.getCpu().getNama());
        System.out.println("Merk CPU              : " + komputer1.getCpu().getMerk());
        System.out.println("Jumlah Core CPU       : " + komputer1.getCpu().getJumlahCore());
        System.out.println("Kecepatan CPU         : " + komputer1.getCpu().getKecepatanGHz() + " GHz");
        System.out.println("Nama Harddrive        : " + komputer1.getHarddrive().getNama());
        System.out.println("Merk Harddrive        : " + komputer1.getHarddrive().getMerk());
        System.out.println("Kapasitas Harddrive   : " + komputer1.getHarddrive().getKapasitasGB() + " GB");
        System.out.println("Tipe Drive Harddrive  : " + komputer1.getHarddrive().getTipeDrive());

        System.out.println("RAM: ");
        int index = 1;
        for (Ram ram : komputer1.getRamList()) {
            System.out.println("  " + index++ + ". Nama          : " + ram.getNama());
            System.out.println("     Merk          : " + ram.getMerk());
            System.out.println("     Kapasitas     : " + ram.getKapasitasGB() + " GB");
            System.out.println("     DDR           : " + ram.getDdr());
        }

        System.out.println("Output Device: ");
        index = 1;
        for (OutputDevice outputDevice : komputer1.getOutputDeviceList()) {
            System.out.println("  " + index++ + ". Nama          : " + outputDevice.getNama());
            System.out.println("     Merk          : " + outputDevice.getMerk());
            System.out.println("     Jenis Output  : " + outputDevice.getJenisOutput());
            System.out.println("     Output Latency: " + outputDevice.getOutputLatency());
        }

        System.out.println("Input Device: ");
        index = 1;
        for (InputDevice inputDevice : komputer1.getInputDeviceList()) {
            System.out.println("  " + index++ + ". Nama          : " + inputDevice.getNama());
            System.out.println("     Merk          : " + inputDevice.getMerk());
            System.out.println("     Jenis Input   : " + inputDevice.getJenisInput());
            System.out.println("     Input Latency : " + inputDevice.getInputLatency());
        }

        System.out.println("Monitor: ");
        index = 1;
        for (Monitor monitor : komputer1.getMonitorList()) {
            System.out.println("  " + index++ + ". Nama          : " + monitor.getNama());
            System.out.println("     Merk          : " + monitor.getMerk());
            System.out.println("     Refresh Rate  : " + monitor.getRefreshRate() + " Hz");
            System.out.println("     Resolution    : " + monitor.getResolution());
        }
        System.out.println("Headset: ");
        System.out.println("Nama          : " + headset1.getNama());
        System.out.println("Merk          : " + headset1.getMerk());
        System.out.println("Jenis Output  : " + headset1.getJenisOutput());
        System.out.println("Output Latency: " + headset1.getOutputLatency());
        System.out.println("isWireless    : " + headset1.isWireless());
        System.out.println("Sound Level   : " + headset1.getSoundLevelDB() + " dB");
    }
}
