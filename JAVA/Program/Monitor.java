package Program;
public class Monitor extends OutputDevice {
    private int refreshRate;
    private String resolution;

    public Monitor() {
    }

    public Monitor(int refreshRate, String resolution, String jenisOutput, String outputLatency, String merk, String nama) {
        super(jenisOutput, outputLatency, merk, nama);
        this.refreshRate = refreshRate;
        this.resolution = resolution;
    }

    public void setRefreshRate(int refreshRate) {
        this.refreshRate = refreshRate;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    public int getRefreshRate() {
        return this.refreshRate;
    }

    public String getResolution() {
        return this.resolution;
    }
}
