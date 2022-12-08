#-*- coding: utf-8 -*-
from threading import Thread
from models.cpu import Cpu

import time

class Device():
    def __init__(self, id, limit, quantum):
        self.id = id
        self.limit = limit
        self.quantum = quantum

        self.workers = []
        self.waiters = []

        self.isOff = False

        Thread(target=self.run).start()

    def __str__(self):
        workers = []
        waiters = []
        
        
        string = '\n {} | {}'.format(self.id, self.limit).upper()
        string += '\n'
        string += ' --------------'
        string += '\n'

        for process in self.workers:
            workers.append(process.pid)

        for process in self.waiters:
            waiters.append(process.pid)

        string += ' worker queue: {}'.format(workers)
        string += '\n'
        string += ' waiters queue: {}'.format(waiters)
        string += '\n'

        return string

    def turnOff(self):
        self.isOff = True 

    def update(self):
        if len(self.workers): 
            self.workers.pop(0)

        if len(self.waiters):
            self.workers.append(self.waiters.pop(0))



    def load(self, process):
        if(process.status == 'waiting'):
            self.workers.append(process) if len(self.workers) < self.limit else self.waiters.append(process)

    def run(self):
        while not self.isOff:

            for process in self.workers:
                if process.status == 'waiting':

                    # ---------------------------
                    process.setStatus('waiting*')
                    # ---------------------------

                    Thread(target=Cpu.run, args=(self.quantum, process, True)).start()
