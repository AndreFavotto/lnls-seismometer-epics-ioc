"""
    This file triggers the first script which starts the system
"""
import sys, traceback as _traceback
from rawFileMonitor import rawFileMonitor
         
try:
    fileMonitor = rawFileMonitor()
    fileMonitor.start()
except Exception as e:
    _traceback.print_exc(file=sys.stdout)
    logmsg = f'Exception raised in processAtrFile.py: {e.args[0]}'
    sys.exit(logmsg)