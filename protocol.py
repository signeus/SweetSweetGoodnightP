from autobahn.twisted.websocket import WebSocketServerProtocol

class CustomProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Cliente conectado: {0}".format(request.peer))

    def onOpen(self):
        self.factory.register(self)
        print("Cliente ha abierto una conexion.")

    def onMessage(self, payload, isBinary):
        print(payload.decode('utf8'))
        if "Sweet-sweet" == payload.decode('utf8'):
            print("Voy a mandar una señal de apagado a todos")
            self.factory.broadcast(u"Goodnight")

    def onClose(self, wasClean, code, reason):
        #WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
        print("Cliente se ha desconectado: {0}".format(reason))
