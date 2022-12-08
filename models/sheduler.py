#-*- coding: utf-8 -*-
from threading import Thread
from random import randint
from models.cpu import Cpu
from view.view import View

class Sheduler():
    # Constructor
    def __init__(self, devices, processes, quantum):

        self.devices = devices 
        self.quantum = quantum         
        self.processTable = processes

        self.doneProcesses = []
        self.nmProcesses = len(processes)

        #viewController
        self.viewController = View(self.processTable, self.doneProcesses, self.devices)

    @property
    # Flag for process in running
    def isRunning(self):
       return len(self.doneProcesses) != self.nmProcesses

    # Get random device
    def getRandomDevice(self):
        return self.devices[randint(0, len(self.devices) - 1)]

    # Update process life times
    def updateLtimes(self, value = 1):
        for process in self.processTable:
            process.ltime += value

        for device in self.devices: 
            for process in device.workers:
                process.ltime += 1

            for process in device.waiters:
                process.ltime += 1

    # Device procedure - Thread function
    def deviceManager(self, processTable, device, process):
        device.load(process)

        # ----------------
        self.viewController.update()
        # ----------------

        #print(' 🔴 {} => {}'.format(process, device))
        self.viewController.logDeviceProcess(process.pid, device.id)
        
        # The process will be ready when process.status == ready
        while( process.status != 'ready'):
            continue
        
        
        device.update()
        process.setDevice()

        #print(' 🟠 {} <= {}'.format(process, device))
        self.viewController.logDeviceProcess(process.pid, device.id, True)

        processTable.append(process)

    #Turn off all devices
    def turnOffDevices(self):
        for device in self.devices:
            device.turnOff()

    #RoundRobin
    def roundRobin(self):
        while self.isRunning:

            if len(self.processTable):

                # --------------------------------
                self.viewController.update()
                # --------------------------------

                #rm first process in processTable
                process = self.processTable.pop(0)

                #setProcess status
                # --------------------------
                process.setStatus('running')
                # --------------------------

                #print(' 🟢 {} => cpu'.format(process.pid))
                self.viewController.logCpuProcess(process.pid)

                #run process in cpu
                Cpu.run(quantum = self.quantum, process = process, isDevice = False, viewController = self.viewController, sheduler = self)

                if process.status == 'waiting' or process.status == 'waiting*':
                    continue

                #set process status
                # -----------------------------------------------------------------------
                process.setStatus('ready') if process.time else process.setStatus('done')
                # -----------------------------------------------------------------------

                #append process status
                self.processTable.append(process) if (process.status == 'ready') else self.doneProcesses.append(process)
            
        # ----------------------------------------------------------------------------
        # FINISH
        print('JÁ ACABOU JÉSSICA?????')
        self.turnOffDevices()   
        # ----------------------------------------------------------------------------

