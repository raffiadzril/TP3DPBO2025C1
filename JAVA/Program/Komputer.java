package Program;
import java.util.List;

public class Komputer {
    private String nama;
    private CPU cpu;
    private List<Ram> ramList;
    private Harddrive harddrive;
    private List<OutputDevice> outputDeviceList;
    private List<InputDevice> inputDeviceList;
    private List<Monitor> monitorList;

    public Komputer() {
    }

    public Komputer(String nama, CPU cpu, List<Ram> ramList, Harddrive harddrive, List<OutputDevice> outputDeviceList, List<InputDevice> inputDeviceList, List<Monitor> monitorList) {
        this.nama = nama;
        this.cpu = cpu;
        this.ramList = ramList;
        this.harddrive = harddrive;
        this.outputDeviceList = outputDeviceList;
        this.inputDeviceList = inputDeviceList;
        this.monitorList = monitorList;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setCpu(CPU cpu) {
        this.cpu = cpu;
    }

    public void setRam(List<Ram> ramList) {
        this.ramList = ramList;
    }

    public void setHarddrive(Harddrive harddrive) {
        this.harddrive = harddrive;
    }

    public void addRam(Ram ram) {
        this.ramList.add(ram);
    }

    public String getNama() {
        return this.nama;
    }

    public CPU getCpu() {
        return this.cpu;
    }

    public List<Ram> getRamList() {
        return this.ramList;
    }

    public Harddrive getHarddrive() {
        return this.harddrive;
    }

    public List<OutputDevice> getOutputDeviceList() {
        return this.outputDeviceList;
    }

    public List<InputDevice> getInputDeviceList() {
        return this.inputDeviceList;
    }

    public List<Monitor> getMonitorList() {
        return this.monitorList;
    }

    public void addOutputDevice(OutputDevice outputDevice) {
        this.outputDeviceList.add(outputDevice);
    }

    public void addInputDevice(InputDevice inputDevice) {
        this.inputDeviceList.add(inputDevice);
    }

    public void addMonitor(Monitor monitor) {
        this.monitorList.add(monitor);
    }

    public void setOutputDeviceList(List<OutputDevice> outputDeviceList) {
        this.outputDeviceList = outputDeviceList;
    }

    public void setInputDeviceList(List<InputDevice> inputDeviceList) {
        this.inputDeviceList = inputDeviceList;
    }

    public void setMonitorList(List<Monitor> monitorList) {
        this.monitorList = monitorList;
    }
}
