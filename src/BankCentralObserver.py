class BankCentralObserver():
    observers = []
    def __init__(self):
        pass

    def attach(self,dataSet):
        if type(dataSet) is tuple:
            self.observers.append(dataSet)
            return True
        return False

    def detach(self, dataDel):
        if dataDel in self.observers:
            self.observers.remove(dataDel)
            return True
        return False

    def notifyObservers(self):
        pass