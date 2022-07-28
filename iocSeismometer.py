"""
    @author: André de Oliveira Águila Favoto
    @create: july, 2022
    @title: Seismometer's IOC
"""
from pcaspy import Driver, SimpleServer
from pcaspy.tools import ServerThread

prefix = 'Met:Seism:'
pvdb   = {
    'Speed-Mon': {
        'unit' : 'm/s'
    },
    'status': {
        'type' : 'char'
    },
    'canal': {
        'type' : 'string'
    },
}

class ioc(Driver):
    def __init__(self):
        super(ioc, self).__init__()
        self.updatePVs()

    def write(self, reason, value):
        self.setParam(reason, value)
        self.updatePVs()
        return True

    def read(self, reason):
        value = self.getParam(reason)
        self.updatePVs()
        return value

server = SimpleServer()
server.createPV(prefix, pvdb)
server_thread = ServerThread(server)
server_thread.start()
