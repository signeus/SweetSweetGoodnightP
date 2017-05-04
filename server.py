from autobahn.twisted.websocket import WebSocketServerFactory

class Server(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = {}

    def GetClient(self, peer):
        return self.clients[peer]

    def broadcast(self, msg):
        for k, v in self.clients.items():
            print(v["client"])
            v["client"].sendMessage(u"Goodnight".encode('utf8'))
            #self.send(v["client"], msg)

    def send(self, client, message):
        client.sendMessage(message)

    def register(self, client):
        if client.peer not in self.clients:
            self.clients[client.peer] = {"client": client}
            print("Registed client: {}".format(client.peer))

    def unregister(self, client):
        if client.peer in self.clients:
            self.clients.pop(client.peer)
            print("Unregisted client: {}".format(client.peer))