from src.BankAccountAdapter import BankAccountAdapter
def driverMain(name,traceObj,amount, receivePort, sendPort):
    obj = BankAccountAdapter(name,traceObj,amount)
    while True:
        received = receivePort.recv()
        if received == "KILL ALL":
            break
        elif received == "SEND":
            nameToSend = input("Nazwa uzytkownika: ")
            amountToSend = input("Wartosc: ")
            obj.sendMoney(nameToSend,amountToSend)
            sendPort.send("OK")
        elif received == "RECEIVE":
            obj.receiveMoney()

