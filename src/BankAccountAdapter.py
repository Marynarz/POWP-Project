from src.BankAccount import BankAccount
from src.SignalTypeEnum import SignalTypeEnum

class BankAccountAdapter(BankAccount):
    traceObj = ''

    def __init__(self,name,traceObj,amount):
        super.__init__(name,traceObj,amount)
        self.traceObj = traceObj

    def __del__(self):
        pass

    def sendMoney(self,name,amount):
        self.sendPort.send((SignalTypeEnum.PRIVSIG,name,amount))
        self.amount = self.amount - amount

    def receiveMoney(self):
        receivedAmount = self.receivePort.recv()
        self.amount = self.amount + int(receivedAmount[2])