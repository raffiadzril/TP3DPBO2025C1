package Program;
public class InputDevice extends Komponen {
    private String jenisInput;
    private String inputLatency;

    public InputDevice() {
    }

    public InputDevice(String jenisInput, String inputLatency, String merk, String nama) {
        super(merk, nama);
        this.jenisInput = jenisInput;
        this.inputLatency = inputLatency;
    }

    public void setJenisInput(String jenisInput) {
        this.jenisInput = jenisInput;
    }

    public void setInputLatency(String inputLatency) {
        this.inputLatency = inputLatency;
    }

    public String getJenisInput() {
        return jenisInput;
    }

    public String getInputLatency() {
        return inputLatency;
    }
}
