from src.CircuitBreakerEnum import CircuitBreakerEnum
from multiprocessing import Pipe


class ServerCircuitBreaker:
    traceCollector = ''
    namePoint = "ServerCircuitCollector"
    circuitStatus = CircuitBreakerEnum.OPEN
    dataQueue = []
    connDict = {}
    receivePort = ''
    sendPort = ''

    def __init__(self,traceCollector):
        self.traceCollector = traceCollector
        self.traceCollector.addTrace("INFO",self.namePoint,"SERVER WELCOME!")
        self.receivePort, self. sendPort = Pipe(duplex=False)

    def __del__(self):
        self.traceCollector.addTrace("INFO", self.namePoint, "SERVER BYE!")

    def receiveSignal(self,recSignal):
        if self.circuitStatus is CircuitBreakerEnum.OPEN:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and self.dataQueue:
            self.dataQueue.append(recSignal)
        elif (self.circuitStatus is CircuitBreakerEnum.CLOSED) and not self.dataQueue:
            pass

    def checkStatus(self, destination):
        if not self.sendSignal(destination,"Connection test"):
            self.circuitStatus = CircuitBreakerEnum.CLOSED

    def sendSignal(self,destId, sourceId, sendSig, statusCheck):
        if statusCheck:
            destId.send("TEST CONNECTION")
            if sourceId.recv():
                return True
            else:
                return False
        else:
            destId.send(sendSig)
            self.receiveSignal(sourceId.recv())
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