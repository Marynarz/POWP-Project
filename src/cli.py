from src.ServerCircuitBreaker import ServerCircuitBreaker
from src.TraceCollect import TraceCollect
from src.BankCentralObserver import BankCentralObserver
from multiprocessing import Process
def main():
    processes = {}
    traceObj = TraceCollect("CLI")
    while True:
        x = input('#: ')
        if x is 0:
            break
        elif x is 1:
            pass
            #processes["serv"] = Process(target=ServerCircuitBreaker,args=traceObj)
        elif x is 2:
            processes["BankCentral"] = BankCentralObserver(traceObj)
            ports = processes["BankCentral"].getConnEnds()
            processes["BankCentral"].start()
        else:
            print("Wrong Command!")
if __name__ == '__main__':
    main()