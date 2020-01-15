###206074###
# centralny serwer bankowy
# wzorzec observer
# obserwator : (nazwa,adres)
# sygnal : [sygnal, nazwa, tresc]

from multiprocessing import Pipe
from multiprocessing import Process
from src.SignalTypeEnum import SignalTypeEnum

class BankCentralObserver(Process):
    observers = []
    traceObj = ''
    namePoint = 'BankCentralObserver'
    sendPort = ''
    receivePort = ''

    def __init__(self,traceObj):
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint, "BANK CENTRAL WELCOME!")
        self.receivePort, self.sendPort = Pipe(duplex=False)
        super(BankCentralObserver,self)

    def __del__(self):
        self.traceObj.addTrace("INFO", self.namePoint, "BANK CENTRAL BYE!")

    def run(self):
        while True:
            if not self.receiveMessage():
                break

    def attach(self,dataSet):
        if type(dataSet) is tuple:
            self.observers.append(dataSet)
            self.traceObj.addTrace("INFO", self.namePoint, "append "+str(dataSet)+" to observers")
            return True
        self.traceObj.addTrace("ERROR", self.namePoint, "append "+str(dataSet)+" failed!")
        return False

    def detach(self, dataDel):
        if dataDel in self.observers:
            self.observers.remove(dataDel)
            self.traceObj.addTrace("INFO", self.namePoint, "removing "+str(dataDel)+" from observers")
            return True
        self.traceObj.addTrace("ERROR", self.namePoint, str(dataDel)+" not found in observers")
        return False

    def notifyObservers(self, sigSend):
        for items in self.observers:
            items[1].send(sigSend)
            self.traceObj.addTrace("INFO", self.namePoint, sigSend+" send to: "+str(items[0]))

    def receiveMessage(self):
        sigRec = self.receivePort.recv()
        self.traceObj.addTrace("INFO", self.namePoint, "receive: "+str(sigRec))
        if sigRec[0] is SignalTypeEnum.BROADCAST:
            self.notifyObservers(sigRec[2])
        elif sigRec[0] is SignalTypeEnum.ATTACH:
            self.attach(tuple(sigRec[2]))
        elif sigRec[0] is SignalTypeEnum.DETACH:
            self.detach(tuple(sigRec[2]))
        elif sigRec[0] is SignalTypeEnum.PRIVSIG:
            self.sendMessage(sigRec[1], sigRec[2])
        elif sigRec[0] is SignalTypeEnum.KILLSIG:
            return False
        return True

    def sendMessage(self, name, sigSend):
        self.sendPort.send([SignalTypeEnum.PRIVSIG, name, sigSend])
        self.traceObj.addTrace("INFO", self.namePoint, "send "+str(sigSend)+" to "+name)

    def getConnEnds(self):
        return (self.sendPort, self.receivePort)