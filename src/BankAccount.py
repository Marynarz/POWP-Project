class BankAccount:
    traceObj =''
    traceName = "BankAccount"

    def __init__(self,traceObj):
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint, "BANK ACCOUNT WELCOME!")

    def __del__(self):
        self.traceObj.addTrace("INFO", self.namePoint, "BANK ACCOUNT BYE!")

    def sendMoney(self):
        pass

    def receiveMoney(self):
        pass