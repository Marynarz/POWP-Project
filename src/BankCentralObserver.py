###206074###
# centralny serwer bankowy
# wzorzec observer
# obserwator : (nazwa,adres)
# sygnal : [sygnal, nazwa, tresc]

from multiprocessing import Pipe
from src.SignalTypeEnum import SignalTypeEnum

class BankCentralObserver():
    observers = []
    traceObj = ''
    namePoint = 'BankCentralObserver'
    sendPort = ''
    receivePort = ''

    def __init__(self,traceObj):
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint, "BANK CENTRAL WELCOME!")
        self.receivePort, self.sendPort = Pipe()


    def attach(self,dataSet):
        if type(dataSet) is tuple:
            self.observers.append(dataSet)
            self.traceObj.addTrace("INFO", self.namePoint, "append "+str(dataSet)+" to observers")
            return True
        self.traceObj.addTrace("ERROR", self.namePoint, "append "+str(dataSet)+" unsuccesful!")
        return False

    def detach(self, dataDel):
        if dataDel in self.observers:
            self.observers.remove(dataDel)
            self.traceObj.addTrace("INFO", self.namePoint, "removing "+str(dataDel)+" from observers")
            return True
        self.traceObj.addTrace("ERROR", self.namePoint, str(dataDel)+" not found in observers")
        return False

    def notifyObservers(self,sigSend):
        for items in self.observers:
            items[1].send(sigSend)
            self.traceObj.addTrace("INFO", self.namePoint, sigSend+" send to: "+str(items[0]))

    def receiveMessage(self):
        sigRec = self.receivePort.recv()
        if sigRec[0] is SignalTypeEnum.BROADCAST:
            self.notifyObservers(sigRec[2])
        elif sigRec[0] is SignalTypeEnum.ATTACH:
            self.attach(tuple(sigRec[2]))
        elif sigRec[0] is SignalTypeEnum.DETACH:
            self.detach(tuple(sigRec[2]))
        elif sigRec[0] is SignalTypeEnum.PRIVSIG:
            pass

    def sendMessage(self,sigSend):
        pass