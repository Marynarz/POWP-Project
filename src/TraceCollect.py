from datetime import datetime
class TraceCollect:
    traceHeader = ""
    traceFile = ""
    def __init__(self,traceName):
        self.traceFile = traceName+".txt"
        with open(self.traceFile,"r") as traceFileHook:
            traceFileHook.write(traceName + " is alive!\n")
            traceFileHook.close()
        self.traceHeader = traceName

    def addTrace(self,traceType,tracePoint,traceMessage):
        message = str(datetime.now().time())+" "+self.traceHeader+": "+traceType+": "+tracePoint+": "+traceMessage
        with open(self.traceFile,"a") as traceFileHook:
            traceFileHook.write(message+"\n")
            traceFileHook.close()

