from src.BankCentralObserver import BankCentralObserver
from src.TraceCollect import TraceCollect
from src.SignalTypeEnum import SignalTypeEnum
from multiprocessing import Pipe

def main():
    traceObj = TraceCollect("BankCentralObserverTest")
    objTested = BankCentralObserver(traceObj)
    namePoint = "TestMain"
    receivePort, sendPort = Pipe()
    dataTuple = ("test",sendPort)

    #port allocation
    ports = objTested.getConnEnds()
    traceObj.addTrace("INFO", namePoint, "ports: "+str(ports))

    #attach
    if objTested.attach(dataTuple):
        traceObj.addTrace("INFO", namePoint, "attach: " + str(dataTuple))
        print("attach complete")
    else:
        traceObj.addTrace("ERROR", namePoint, "attach unsuccesfull: " + str(dataTuple))
        print("attach failed")

    #attach failed
    if objTested.attach(str(dataTuple)):
        traceObj.addTrace("INFO", namePoint, "attach: " + str(dataTuple))
        print("attach complete")
    else:
        traceObj.addTrace("ERROR", namePoint, "attach failed: " + str(dataTuple))
        print("attach failed")

    #broadcast
    testMessage = "TEST polaczenia!!!"
    objTested.notifyObservers(testMessage)
    if receivePort.recv() == testMessage:
        print("Broadcast ok")
        traceObj.addTrace("INFO", namePoint, "broadcast ok")
    else:
        print("Broadcast NOK")
        traceObj.addTrace("ERROR", namePoint, "broadcast NOK")

    #sending message
    mess = "Dupa123"
    name = "Piotrus Pan"
    objTested.sendMessage(name,mess)
    received = ports[1].recv()
    if received == [SignalTypeEnum.PRIVSIG,name,mess]:
        print("send ok")
        traceObj.addTrace("INFO", namePoint, "received: "+str(received))
    else:
        traceObj.addTrace("ERROR", namePoint, "send failed")

    #attach
    if objTested.detach(dataTuple):
        traceObj.addTrace("INFO", namePoint, "detach: " + str(dataTuple))
        print("detach complete")
    else:
        traceObj.addTrace("ERROR", namePoint, "detach unsuccesfull: " + str(dataTuple))
        print("detach failed")

    #attach failed
    if objTested.detach(str(dataTuple)):
        traceObj.addTrace("INFO", namePoint, "detach: " + str(dataTuple))
        print("detach complete")
    else:
        traceObj.addTrace("ERROR", namePoint, "detach failed: " + str(dataTuple))
        print("detach failed")

if __name__ == '__main__':
    main()