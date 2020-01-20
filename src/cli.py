from src.BankCentralObserver import BankCentralObserver
from src.SignalTypeEnum import SignalTypeEnum
from src.TraceCollect import TraceCollect
from src.ServerCircuitBreaker import ServerCircuitBreaker
from src.BankAccountAdapter import BankAccountAdapter


def main():
    processes = {}
    traceObj = TraceCollect("CLI")
    helpMenu()
    ports = []
    while True:
        x = input('#: ')
        if x is "0":
            for entires in ports:
                entires[0].send([SignalTypeEnum.KILLSIG,0])
                print(entires)
            break
        elif x is "1":
            processes["serv"] = ServerCircuitBreaker(traceObj)
        elif x is "2":
            processes["BankCentral"] = BankCentralObserver(traceObj)
            ports.append(processes["BankCentral"].getConnEnds())
            processes["BankCentral"].start()
        elif x is "3":
            accName = input("Nazwa konta: ")
            accAmount = input("Saldo poczatkowe: ")
            processes[accName] = BankAccountAdapter(accName,traceObj,accAmount)
            ports.append(processes[accName].getConnEnds())
            processes[accName].start()
        elif x is "h":
            helpMenu()
        else:
            print("Wrong Command!")

def helpMenu():
    print("---POWP PROJEKT---")
    print("Robenie przelewow")
    print("Wykorzystane wzorce: Observer, adapter, cirguit braker")
    print()
    print("Komendy CLI:")
    print("0 - exit")
    print("1 - start circuit breakera -- nie aktywne")
    print("2 - start centrali bank account - observer")
    print("3 - start cank account adapter - adapter")
    print("h - pomoc")
    print("---")

if __name__ == '__main__':
    main()