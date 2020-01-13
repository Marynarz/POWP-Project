
class ServerCircuitBreaker:
    traceCollector = ''
    namePoint = "ServerCircuitCollector"
    def __init__(self,traceCollector):
        self.traceCollector = traceCollector
        self.traceCollector.addTrace("INFO",self.namePoint,"SERVER WELCOME!")