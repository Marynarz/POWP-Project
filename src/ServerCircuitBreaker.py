from multiprocessing import Pipe
from multiprocessing import Process
from src.SignalTypeEnum import SignalTypeEnum
from src.CircuitBreakerEnum import CircuitBreakerEnum


class ServerCircuitBreaker(Process):
    traceCollector = ''
    namePoint = "ServerCircuitCollector"
    circuitStatus = CircuitBreakerEnum.OPEN
    dataQueue = []
    connDict = {}
    receivePort = ''
    sendPort = ''

    def __init__(self,traceCollector):
        super(ServerCircuitBreaker,self).__init__()
        self.traceCollector = traceCollector
        self.traceCollector.addTrace("INFO",self.namePoint,"SERVER WELCOME!")
        self.receivePort, self.sendPort = Pipe(duplex=False)

    def __del__(self):
        pass

    def run(self):
        while True:
            received = self.receivePort.recv()
            if received[0] == SignalTypeEnum.KILLSIG:
                self.traceObj.addTrace("INFO", self.namePoint, "SERVER BYE!")
                break
            else:
                self.receiveSignal(received)


    def receiveSignal(self,rec):
        recSignal = rec
        if recSignal[0] == "TEST OK":
            return True
        elif recSignal [0] != "TEST OK" and self.circuitStatus is CircuitBreakerEnum.OPEN:
            return False
        elif recSignal[0] is SignalTypeEnum.REGISTER:
            self.registerService(recSignal[1],recSignal[2])
        if self.circuitStatus is CircuitBreakerEnum.OPEN:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and self.dataQueue:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and not self.dataQueue:
            pass
        return True

    def checkStatus(self):
        for key in self.connDict:
            if not self.sendSignal(self.connDict[key],"Connection test",True):
                self.circuitStatus = CircuitBreakerEnum.CLOSED

    def sendSignal(self,name, sendSig, statusCheck):
        if statusCheck:
            self.connDict[name].send("TEST")
            receive = self.receivePort.recv()
            if not self.receiveSignal():
                return True
            else:
                return False
        else:
            self.connDict[name].send(sendSig)
        return True

    def clearQueue(self):
        if self.dataQueue and self.circuitStatus is CircuitBreakerEnum.CLOSED:
            self.sendSignal(self.dataQueue.pop[0])
            self.checkStatus()
            self.clearQueue()
        elif self.dataQueue and self.circuitStatus is CircuitBreakerEnum.OPEN:
            self.checkStatus()
            self.clearQueue()
        elif not self.dataQueue:
            pass

    def registerService(self,connId,connName):
        self.connDict[connName] = connId

    def getConnEnds(self):
        return (self.sendPort, self.receivePort)
