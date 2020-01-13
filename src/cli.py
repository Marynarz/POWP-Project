from src.ServerCircuitBreaker import ServerCircuitBreaker
from src.TraceCollect import TraceCollect
from multiprocessing import Process
def main():
    processes = {}
    traceObj = TraceCollect("CLI")
    while True:
        x = input('#: ')
        if x is 0:
            break
        elif x is 1:
            processes["serv"] = Process(target=ServerCircuitBreaker,args=traceObj)
        else:
            print("Wrong Command!")
if __name__ == '__main__':
    main()