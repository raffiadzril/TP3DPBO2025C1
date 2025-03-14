#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Cpu.cpp"
#include "Harddrive.cpp"
#include "Ram.cpp"
#include "OutputDevice.cpp"
#include "InputDevice.cpp"
#include "Monitor.cpp"

using namespace std;


class Komputer
{
private:
    string nama;
    CPU cpu;
    vector<Ram> ramList;
    Harddrive harddrive;
    vector<OutputDevice> outputDeviceList;
    vector<InputDevice> inputDeviceList;
    vector<Monitor> monitorList;
    
public:
    Komputer()
    {


    }


    Komputer(string nama, CPU cpu, vector<Ram> ramList, Harddrive harddrive, vector<OutputDevice> outputDeviceList, vector<InputDevice> inputDeviceList, vector<Monitor> monitorList)
    {
        this->nama = nama;
        this->cpu = cpu;
        this->ramList = ramList;
        this->harddrive = harddrive;
        this->outputDeviceList = outputDeviceList;
        this->inputDeviceList = inputDeviceList;
        this->monitorList = monitorList;
    }


    void setNama(string nama)
    {
        this->nama = nama;
    }

    void setCpu(CPU cpu)
    {
        this->cpu = cpu;
    }


    void setRam(vector<Ram> ramList)
    {
        this->ramList = ramList;
    }    
   
    void setHarddrive(Harddrive harddrive)
    {
        this->harddrive = harddrive;
    }


    void addRam(Ram ram)
    {
        this->ramList.push_back(ram);
    }


    string getNama()
    {
        return this->nama;
    }


    CPU getCpu()
    {
        return this->cpu;
    }


    vector<Ram> getRamList() // return vector
    {
        return this->ramList;
    }


    Harddrive getHarddrive()
    {
        return this->harddrive;
    }
    vector<OutputDevice> getOutputDeviceList()
    {
        return this->outputDeviceList;
    }
    vector<InputDevice> getInputDeviceList()
    {
        return this->inputDeviceList;
    }
    vector<Monitor> getMonitorList()
    {
        return this->monitorList;
    }
    void addOutputDevice(OutputDevice outputDevice)
    {
        this->outputDeviceList.push_back(outputDevice);
    }
    void addInputDevice(InputDevice inputDevice)
    {
        this->inputDeviceList.push_back(inputDevice);
    }
    void addMonitor(Monitor monitor)
    {
        this->monitorList.push_back(monitor);
    }

    void setOutputdevice(vector<OutputDevice> outputDeviceList)
    {
        this->outputDeviceList = outputDeviceList;
    }
    void setInputdevice(vector<InputDevice> inputDeviceList)
    {
        this->inputDeviceList = inputDeviceList;
    }
    void setMonitor(vector<Monitor> monitorList)
    {
        this->monitorList = monitorList;
    }
    


    ~Komputer()
    {


    }
};
