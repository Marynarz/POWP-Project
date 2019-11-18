class TraceCollect:
    traceHeader = ""
    def __init__(self,traceName):
        with open(traceName+".txt","a") as traceFileHook:
            traceFileHook.write(traceName + " is alive!")
            traceFileHook.close()
        self.traceHeader = traceName

    def 
