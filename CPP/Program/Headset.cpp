#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"
#include "OutputDevice.cpp"
#include "InputDevice.cpp"

class Headset : public OutputDevice, public InputDevice {
    private:
        bool isWireless;
        int soundLevelDB;
    public:
        Headset() {

        }

        Headset(bool isWireless, int soundLevelDB, string jenisOutput, string OutputLatency, string jenisInput, string inputLatency, string merk, string nama) : 
            OutputDevice(jenisOutput, OutputLatency, merk, nama), 
            InputDevice(jenisInput, inputLatency, merk, nama) {
            this->isWireless = isWireless;
            this->soundLevelDB = soundLevelDB;
        }

        void setIsWireless(bool isWireless) {
            this->isWireless = isWireless;
        }

        void setSoundLevelDB(int soundLevelDB) {
            this->soundLevelDB = soundLevelDB;
        }

        bool getIsWireless() {
            return this->isWireless;
        }

        int getSoundLevelDB() {
            return this->soundLevelDB;
        }

        ~Headset() {

        }

};