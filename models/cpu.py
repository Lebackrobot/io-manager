#-*- coding: utf-8 -*-
from abc import abstractmethod
from threading import Thread
import time

#processador - add ltime and sub tume
#device - add ltime (device is slower)

class Cpu():

    @abstractmethod
    #only execute processes
    def run(quantum, process, isDevice = False, viewController = None, sheduler = None):

        if( isDevice ):

            #nerf device
            time.sleep(1)

            for i in range(quantum): continue

            # ------------------------
            process.setStatus('ready')
            # ------------------------

        else:

            viewController.log(cpuProcess = process)

            for i in range(quantum):

                if(process.time):
                    
                    sheduler.updateLtimes()
                    process.ltime += 1

                    if process.requestIO:
                        # --------------------------
                        process.setStatus('waiting')
                        # --------------------------

                        device = sheduler.getRandomDevice()
                        process.setDevice(device.id)

                        Thread(target=sheduler.deviceManager, args=(sheduler.processTable, device, process)).start()
                        break

                    else:

                        viewController.update()

                        #process.ltime +=  1
                        process.time  -=  1


                else:
                    viewController.update()
                    continue


        
                #Gambiarra para compensar o update do loop do sheuduler
                #------------------------
                #sheduler.updateLtimes(-1)
                #viewController.update(-1)
                #------------------------
