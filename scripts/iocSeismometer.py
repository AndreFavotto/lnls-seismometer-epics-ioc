"""
    @author: André de Oliveira Águila Favoto
    @create: july, 2022
    @title: Seismometer's IOC
"""
import sys, traceback as _traceback
from pcaspy import Driver, SimpleServer
from pcaspy.tools import ServerThread
from globalVars import globalVars

prefix = f'{globalVars.getArgs().P}'
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
    driver = ioc()
except Exception:
    _traceback.print_exc(file=sys.stdout)
    sys.exit("Exception raised in iocSeismometer.py")