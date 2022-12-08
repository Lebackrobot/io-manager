#-*- coding: utf-8 -*-
from prettytable import PrettyTable
from threading import Lock

class View():
    def __init__(self, processTable, doneProcesses, devices):
        self.processTable = processTable
        self.doneProcesses = doneProcesses
        self.devices = devices

        self.time = 0

    def update(self, quantum = 1):
        self.time += quantum

    def logDeviceProcess(self, process, device, isOut = False):
        if(not isOut):
            Lock()
            print('\n ·  ⏰ Loop:', self.time, '(👇)', '\n ·  🔴 {} => {}'.format(process, device))


        else:
            Lock()
            print('\n ·· ⏰ Loop:', self.time, '(👇)',  '\n ·· 🟠 {} <= {}'.format(process, device))


    def logCpuProcess(self, process):
            Lock()
            print('\n ··· ⏰ Loop:', self.time, '(👇)' + '\n ··· 🟢 {} => cpu'.format(process))

    def log(self, cpuProcess):
        Lock()
        
        # create table
        viewProcessTable = PrettyTable(['pid', 'time', 'ltime', 'status', 'device'])

        # align columns
        viewProcessTable.align['pid']    = "c"
        viewProcessTable.align['time']   = "c"
        viewProcessTable.align['ltime']  = "c"
        viewProcessTable.align['status'] = "c"
        viewProcessTable.align['device'] = "c"

        #Creat view processTable
        # --------------------------------------------------------------------------------------------------
        viewProcessTable.add_row([cpuProcess.pid, cpuProcess.time, cpuProcess.ltime, cpuProcess.status, cpuProcess.device])

        for process in self.processTable:
            viewProcessTable.add_row([process.pid, process.time, process.ltime, process.status, process.device])


        for device in self.devices:
            for process in device.workers:
                viewProcessTable.add_row([process.pid, process.time, process.ltime, process.status, process.device])

            for process in device.waiters:
                viewProcessTable.add_row([process.pid, process.time, process.ltime, process.status, process.device])


        for process in self.doneProcesses:
            viewProcessTable.add_row([process.pid, process.time, process.ltime, process.status, process.device])
        # --------------------------------------------------------------------------------------------------

        #Creat process table
        # --------------------------------------------------------------------------------------------------
        deviceTable = PrettyTable(['device'.upper(), 'limit', 'workers', 'waiters'])
        for device in self.devices:
            
            workers = []
            waiters = []
            
            for process in device.workers:
                workers.append(process.pid)

            for process in device.waiters:
                waiters.append(process.pid)

            deviceTable.add_row([device.id.upper(), device.limit, '{}'.format(workers), '{}'.format(waiters)])
        # --------------------------------------------------------------------------------------------------

        # -------------------------------------------
        print('\n \033[42m Process Table: \033[0;0m')
        print(viewProcessTable)

        
        print('\n \033[41m Devices:  \033[0;0m')
        print(deviceTable)
        # ------------------------------------------

