###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Crossbar.io Technologies GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
import subprocess

class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Cliente conectado!: {0}".format(response.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        self.sendMessage(u"Hi!!".encode('utf8'))
        #def hello():
        #    self.sendMessage(u"Hello, world!".encode('utf8'))
        #    self.sendMessage(b"\x00\x01\x03\x04", isBinary=True)
        #    #self.factory.reactor.callLater(1, hello)

        # start sending messages every second ..
        #hello()

    def onMessage(self, payload, isBinary):
        if u"Goodnight" == payload.decode('utf8'):
            print("Voy apagando el PC")
            subprocess.call(["shutdown", "/s", "/f"])

    def onClose(self, wasClean, code, reason):
        print("Conexion cerrada: {0}".format(reason))


if __name__ == '__main__':

    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketClientFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MyClientProtocol

    reactor.connectTCP("127.0.0.1", 9000, factory)
    reactor.run()