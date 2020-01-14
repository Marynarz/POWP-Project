from multiprocessing import Pipe
from src.SignalTypeEnum import SignalTypeEnum

class BankAccount:
    traceObj =''
    traceName = "BankAccount"
    selfName = ""
    receivePort = ''
    sendPort = ''
    amount = 0
    def __init__(self,name,traceObj,amount=0):
        self.amount = amount
        self.selfName = name
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint, "BANK ACCOUNT WELCOME!")
        self.receivePort, self.sendPort = Pipe(duplex=False)

    def __del__(self):
        self.traceObj.addTrace("INFO", self.namePoint, "BANK ACCOUNT BYE!")

    def sendMoney(self,name,amount):
        pass
        #self.sendPort.send((SignalTypeEnum.PRIVSIG,name,amount))
        #self.amount = self.amount - amount

    def receiveMoney(self):
        pass
        #receivedAmount = self.receivePort.recv()
        #self.amount = self.amount + int(receivedAmount[2])