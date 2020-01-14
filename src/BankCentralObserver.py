###206074###
# centralny serwer bankowy
# wzorzec observer
# obserwator : (nazwa,adres)

class BankCentralObserver():
    observers = []
    traceObj = ''
    traceName = 'BankCentralObserver'

    def __init__(self,traceObj):
        self.traceObj = traceObj
        self.traceObj.addTrace("INFO", self.namePoint, "BANK CENTRAL WELCOME!")

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