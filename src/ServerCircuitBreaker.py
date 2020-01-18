from multiprocessing import Pipe
from multiprocessing import Process

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
        self.traceCollector.addTrace("INFO", self.namePoint, "SERVER BYE!")

    def run(self):
        pass

    def receiveSignal(self):
        recSignal = self.receivePort.recv()
        if recSignal[1] == "TEST OK":
            return True
        elif recSignal [1] != "TEST OK" and self.circuitStatus is CircuitBreakerEnum.OPEN:
            return False
        if self.circuitStatus is CircuitBreakerEnum.OPEN:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and self.dataQueue:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and not self.dataQueue:
            pass
        return True

    def checkStatus(self, destination):
        if not self.sendSignal(destination,"Connection test",True):
            self.circuitStatus = CircuitBreakerEnum.CLOSED

    def sendSignal(self,name, sendSig, statusCheck):
        if statusCheck:
            self.connDict[name].send("TEST CONNECTION")
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
