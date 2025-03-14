package Program;
public class Headset extends OutputDevice {
    private boolean isWireless;
    private int soundLevelDB;

    // Default constructor
    public Headset() {}

    // Complete constructor
    public Headset(boolean isWireless, int soundLevelDB, String jenisOutput, String outputLatency, String merk, String nama) {
        super(jenisOutput, outputLatency, merk, nama);
        this.isWireless = isWireless;
        this.soundLevelDB = soundLevelDB;
    }

    // Setter
    public void setWireless(boolean isWireless) {
        this.isWireless = isWireless;
    }

    public void setSoundLevelDB(int soundLevelDB) {
        this.soundLevelDB = soundLevelDB;
    }

    // Getter
    public boolean isWireless() {
        return isWireless;
    }

    public int getSoundLevelDB() {
        return soundLevelDB;
    }
}
