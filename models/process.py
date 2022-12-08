#-*- coding: utf-8 -*-
from random import randint

class Process():
    def __init__(self, pid, time, probRequestIO):
            
            
            self.probRequestIO = probRequestIO
            
            self.pid = pid
            self.time = time
            self.ltime = 0
            self.status = 'ready'

            self.device = '-'


    def __str__(self):
        return '{}  {}     {}     {}      {}'.format(self.pid, self.time, self.ltime, self.status, self.device)

    def setStatus(self, value):
        self.status = value
    
    def setDevice(self, device='-'):
        self.device = device


    @property
    def requestIO(self):
        return True if randint(0, 100) <= self.probRequestIO else False