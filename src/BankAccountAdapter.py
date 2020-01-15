from src.BankAccount import BankAccount
from src.SignalTypeEnum import SignalTypeEnum
from multiprocessing import Process

class BankAccountAdapter(Process,BankAccount):
    traceObj = ''

    def __init__(self,name,traceObj,amount):
        BankAccount.__init__(name,traceObj,amount)
        Process(BankAccountAdapter, self).__init__()
        self.traceObj = traceObj

    def __del__(self):
        pass

    def run(self):
        while True:
            received = self.receivePort.recv()
            if received[0] == SignalTypeEnum.KILLSIG:
                break
            elif received[0] == SignalTypeEnum.PRIVSIG:
                self.receiveMoney(int(received[2]))
            else:
                pass


    def sendMoney(self,name,amount):
        self.sendPort.send((SignalTypeEnum.PRIVSIG,name,amount))
        self.amount = self.amount - amount

    def receiveMoney(self,amount):
        #receivedAmount = self.receivePort.recv()
        self.amount = self.amount + amount