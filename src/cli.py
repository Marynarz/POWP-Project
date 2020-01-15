from src.ServerCircuitBreaker import ServerCircuitBreaker
from src.TraceCollect import TraceCollect
from src.BankCentralObserver import BankCentralObserver
from src.SignalTypeEnum import SignalTypeEnum
from src.BankAccountAdapter import BankAccountAdapter
from multiprocessing import Process
def main():
    processes = {}
    traceObj = TraceCollect("CLI")
    helpMenu()
    while True:
        x = input('#: ')
        if x is "0":
            for entires in processes:
                processes[entires].send([SignalTypeEnum.KILLSIG,0])
                processes[entires].join()
                print(entires)
            break
        elif x is "1":
            pass
            #processes["serv"] = Process(target=ServerCircuitBreaker,args=traceObj)
        elif x is "2":
            processes["BankCentral"] = BankCentralObserver(traceObj)
            ports = processes["BankCentral"].getConnEnds()
            processes["BankCentral"].start()
        elif x is "3":
            accName = input("Nazwa konta: ")
            accAmount = input("Saldo poczatkowe: ")
            processes[accName] = BankAccountAdapter(accName,traceObj,accAmount)
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
    print("2 - start centrali bnak account - observer")
    print("h - pomoc")

if __name__ == '__main__':
    main()