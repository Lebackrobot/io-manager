#-*- coding: utf-8 -*-
from models.device import Device
from models.process import Process
from models.sheduler import Sheduler

if __name__ == '__main__':

    document = open('./files/input.txt').read().split('\n')

    devices   = []
    processes = []

    #get props: quantum and number of devices
    # ----------------------------------------
    quantum   = int(document[0].split('|')[0])
    nmDevices = int(document[0].split('|')[1])
    # ----------------------------------------

    for index, line in enumerate(document):
        line = line.split('|')

        if index:
            if index < nmDevices + 1:
                # creat devices
                # --------------------------------------------------------------------------------
                devices.append(Device(id = line[0], limit = int(line[1]), quantum = int(line[2])))
                # --------------------------------------------------------------------------------

            else:
                # create process
                # -----------------------------------------------------------------------------------------
                processes.append(Process(pid = line[0], time = int(line[1]), probRequestIO = int(line[2])))
                # -----------------------------------------------------------------------------------------

    #creat sheduler
    sheduler = Sheduler(devices, processes, quantum)
    sheduler.roundRobin()