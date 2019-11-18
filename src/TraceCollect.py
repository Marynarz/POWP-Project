from datetime import datetime
class TraceCollect:
    traceHeader = ""
    traceFile = ""
    def __init__(self,traceName):
        self.traceFile = traceName+".txt"
        with open(self.traceFile,"a") as traceFileHook:
            traceFileHook.write(traceName + " is alive!")
            traceFileHook.close()
        self.traceHeader = traceName

    def addTrace(self,traceType,traceMessage):
        message = datetime.now().time() + " " + self.traceHeader + ": " + traceType + ": " + traceMessage
        with open(self.traceFile,"a") as traceFileHook:
            traceFileHook.write(message)
            traceFileHook.close()
            
