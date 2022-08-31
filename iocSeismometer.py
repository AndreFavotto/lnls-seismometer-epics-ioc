"""
    @author: André de Oliveira Águila Favoto
    @create: july, 2022
    @title: Seismometer's IOC
"""
import os
from pcaspy import Driver, SimpleServer
from pcaspy.tools import ServerThread

prefix = 'RR-09S:SS-Seism-Ax13:'
pvdb   = {
    'S-Mon': {
        'unit' : 'm/s'
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

try:
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    server_thread = ServerThread(server)
    server_thread.start()
except Exception as e:
    print(f'Error starting epics server: {e.args[0]}')
    os._exit(1)