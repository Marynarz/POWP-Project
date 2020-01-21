from multiprocessing import Process

from src.BankAccount import BankAccount
from src.SignalTypeEnum import SignalTypeEnum


class BankAccountAdapter(Process,BankAccount):
    traceObj = ''
    namePoint2 = 'BankAccountAdapter'

    def __init__(self,name,traceObj,amount):
        BankAccount.__init__(self,name,traceObj,amount)
        super(BankAccountAdapter, self).__init__()
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint2, "BANK ACCOUNT ADAPTER WELCOME!")

    def __del__(self):
        pass

    def run(self):
        while True:
            received = self.receivePort.recv()
            if received[0] == SignalTypeEnum.KILLSIG:
                self.traceObj.addTrace("INFO", self.namePoint2, "BANK ACCOUNT ADAPTER BYE!")
                break
            elif received[0] == SignalTypeEnum.PRIVSIG:
                self.traceObj.addTrace("INFO", self.namePoint2, "Received = "+str(received))
                self.receiveMoney(int(received[2]))
            elif received[0] == "TEST":
                self.sendPort.send("TEST OK")
                self.traceObj.addTrace("TEST", self.namePoint2, "Received = TEST, send TEST OK")
            else:
                pass


    def sendMoney(self,name,amount):
        self.sendPort.send((SignalTypeEnum.PRIVSIG,name,amount))
        self.amount = self.amount - amount

    def getConnEnds(self):
        return (self.sendPort, self.receivePort)

    def receiveMoney(self,amount):
        #receivedAmount = self.receivePort.recv()
        self.amount = self.amount + amount
        self.traceObj.addTrace("INFO", self.namePoint2, "New amount: "+str(self.getAmount()))
    def attachToServer(self):
        self.sendPort(SignalTypeEnum.ATTACH,self.name,self.sendPort)