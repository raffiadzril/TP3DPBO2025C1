from CPU import CPU
from Ram import Ram
from Harddrive import Harddrive
from OutputDevice import OutputDevice
from InputDevice import InputDevice
from Monitor import Monitor
from Komponen import Komponen

class Komputer:
    def __init__(self, nama="", cpu=CPU(), ramList=[], harddrive=Harddrive(), outputDeviceList=[], inputDeviceList=[], monitorList=[]):
        self.nama = nama
        self.cpu = cpu
        self.ramList = ramList
        self.harddrive = harddrive
        self.outputDeviceList = outputDeviceList
        self.inputDeviceList = inputDeviceList
        self.monitorList = monitorList

    def setNama(self, nama):
        self.nama = nama

    def setCpu(self, cpu):
        self.cpu = cpu

    def setRam(self, ramList):
        self.ramList = ramList

    def setHarddrive(self, harddrive):
        self.harddrive = harddrive

    def addRam(self, ram):
        self.ramList.append(ram)

    def getNama(self):
        return self.nama

    def getCpu(self):
        return self.cpu

    def getRamList(self):
        return self.ramList

    def getHarddrive(self):
        return self.harddrive

    def getOutputDeviceList(self):
        return self.outputDeviceList

    def getInputDeviceList(self):
        return self.inputDeviceList

    def getMonitorList(self):
        return self.monitorList

    def addOutputDevice(self, outputDevice):
        self.outputDeviceList.append(outputDevice)

    def addInputDevice(self, inputDevice):
        self.inputDeviceList.append(inputDevice)

    def addMonitor(self, monitor):
        self.monitorList.append(monitor)

    def setOutputdevice(self, outputDeviceList):
        self.outputDeviceList = outputDeviceList

    def setInputdevice(self, inputDeviceList):
        self.inputDeviceList = inputDeviceList

    def setMonitor(self, monitorList):
        self.monitorList = monitorList





# #pragma once
# #include <iostream>
# #include <string>
# #include <vector>
# #include "Cpu.cpp"
# #include "Harddrive.cpp"
# #include "Ram.cpp"
# #include "OutputDevice.cpp"
# #include "InputDevice.cpp"
# #include "Monitor.cpp"

# using namespace std;


# class Komputer
# {
# private:
#     string nama;
#     CPU cpu;
#     vector<Ram> ramList;
#     Harddrive harddrive;
#     vector<OutputDevice> outputDeviceList;
#     vector<InputDevice> inputDeviceList;
#     vector<Monitor> monitorList;
    
# public:
#     Komputer()
#     {


#     }


#     Komputer(string nama, CPU cpu, vector<Ram> ramList, Harddrive harddrive, vector<OutputDevice> outputDeviceList, vector<InputDevice> inputDeviceList, vector<Monitor> monitorList)
#     {
#         this->nama = nama;
#         this->cpu = cpu;
#         this->ramList = ramList;
#         this->harddrive = harddrive;
#         this->outputDeviceList = outputDeviceList;
#         this->inputDeviceList = inputDeviceList;
#         this->monitorList = monitorList;
#     }


#     void setNama(string nama)
#     {
#         this->nama = nama;
#     }

#     void setCpu(CPU cpu)
#     {
#         this->cpu = cpu;
#     }


#     void setRam(vector<Ram> ramList)
#     {
#         this->ramList = ramList;
#     }    
   
#     void setHarddrive(Harddrive harddrive)
#     {
#         this->harddrive = harddrive;
#     }


#     void addRam(Ram ram)
#     {
#         this->ramList.push_back(ram);
#     }


#     string getNama()
#     {
#         return this->nama;
#     }


#     CPU getCpu()
#     {
#         return this->cpu;
#     }


#     vector<Ram> getRamList() // return vector
#     {
#         return this->ramList;
#     }


#     Harddrive getHarddrive()
#     {
#         return this->harddrive;
#     }
#     vector<OutputDevice> getOutputDeviceList()
#     {
#         return this->outputDeviceList;
#     }
#     vector<InputDevice> getInputDeviceList()
#     {
#         return this->inputDeviceList;
#     }
#     vector<Monitor> getMonitorList()
#     {
#         return this->monitorList;
#     }
#     void addOutputDevice(OutputDevice outputDevice)
#     {
#         this->outputDeviceList.push_back(outputDevice);
#     }
#     void addInputDevice(InputDevice inputDevice)
#     {
#         this->inputDeviceList.push_back(inputDevice);
#     }
#     void addMonitor(Monitor monitor)
#     {
#         this->monitorList.push_back(monitor);
#     }

#     void setOutputdevice(vector<OutputDevice> outputDeviceList)
#     {
#         this->outputDeviceList = outputDeviceList;
#     }
#     void setInputdevice(vector<InputDevice> inputDeviceList)
#     {
#         this->inputDeviceList = inputDeviceList;
#     }
#     void setMonitor(vector<Monitor> monitorList)
#     {
#         this->monitorList = monitorList;
#     }
    


#     ~Komputer()
#     {


#     }
# };
