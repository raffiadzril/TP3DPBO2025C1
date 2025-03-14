#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"
#include "OutputDevice.cpp"

class Monitor : public OutputDevice {
    private:
        int refreshRate;
        string resolution;
    public:
        Monitor() {

        }

        Monitor(int refreshRate, string resolution, string jenisOutput, string OutputLatency, string merk, string nama) : 
            OutputDevice(jenisOutput, OutputLatency, merk, nama) {
            this->refreshRate = refreshRate;
            this->resolution = resolution;
        }

        void setRefreshRate(int refreshRate) {
            this->refreshRate = refreshRate;
        }

        void setResolution(string resolution) {
            this->resolution = resolution;
        }

        int getRefreshRate() {
            return this->refreshRate;
        }

        string getResolution() {
            return this->resolution;
        }

        ~Monitor() {

        }

};