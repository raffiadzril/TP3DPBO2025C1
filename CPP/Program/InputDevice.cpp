#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"

class InputDevice : public Komponen {
    private:
        string jenisInput;
        string inputLatency;
    public:
        InputDevice() {

        }

        InputDevice(string jenisInput, string inputLatency, string merk, string nama) : Komponen(merk, nama) {
            this->jenisInput = jenisInput;
            this->inputLatency = inputLatency;
        }

        void setJenisInput(string jenisInput) {
            this->jenisInput = jenisInput;
        }

        void setInputLatency(string inputLatency) {
            this->inputLatency = inputLatency;
        }

        string getJenisInput() {
            return this->jenisInput;
        }

        string getInputLatency() {
            return this->inputLatency;
        }

        ~InputDevice() {

        }
};