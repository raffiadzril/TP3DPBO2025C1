package Program;
public class OutputDevice extends Komponen {
    private String jenisOutput;
    private String outputLatency;

    public OutputDevice() {
    }

    public OutputDevice(String jenisOutput, String outputLatency, String merk, String nama) {
        super(merk, nama);
        this.jenisOutput = jenisOutput;
        this.outputLatency = outputLatency;
    }

    public void setJenisOutput(String jenisOutput) {
        this.jenisOutput = jenisOutput;
    }

    public void setOutputLatency(String outputLatency) {
        this.outputLatency = outputLatency;
    }

    public String getJenisOutput() {
        return jenisOutput;
    }

    public String getOutputLatency() {
        return outputLatency;
    }
}
