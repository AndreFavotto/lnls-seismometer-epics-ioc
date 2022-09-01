"""
    This file triggers the first script which starts the system
"""
import traceback as _traceback, sys
from rawFileMonitor import rawFileMonitor
         
try:
    fileMonitor = rawFileMonitor()
    fileMonitor.start()
except Exception:
    _traceback.print_exc(file=sys.stdout)
    sys.exit('Exception raised in main.py')
