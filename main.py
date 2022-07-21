"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 30, 2020
    @modified: july, 2022
    @title: main
"""

# Libraries
import time
from rawFileMonitor import RawFileMonitor
from iocSeismometer import ioc 

# Start the software
file = open("start.txt", "r")
start = bool(file.read())
file.close()

if start == True:
    # Instantiate classes
    fileMonitor = RawFileMonitor()
    iocServer = ioc()
    fileMonitor.start()
    while start == True:
        time.sleep(60)
        file = open("start.txt", "r")
        start = bool(int(file.read()))
        file.close()

fileMonitor.stop()
iocServer.stop()