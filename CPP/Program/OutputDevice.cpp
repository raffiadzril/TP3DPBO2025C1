#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"

class OutputDevice : public Komponen {
    private:
        string jenisOutput;
        string OutputLatency;
    public:
        OutputDevice() {

        }

        OutputDevice(string jenisOutput, string OutputLatency, string merk, string nama) : Komponen(merk, nama) {
            this->jenisOutput = jenisOutput;
            this->OutputLatency = OutputLatency;
        }

        void setJenisOutput(string jenisOutput) {
            this->jenisOutput = jenisOutput;
        }

        void setOutputLatency(string OutputLatency) {
            this->OutputLatency = OutputLatency;
        }

        string getJenisOutput() {
            return this->jenisOutput;
        }

        string getOutputLatency() {
            return this->OutputLatency;
        }

        ~OutputDevice() {

        }
};