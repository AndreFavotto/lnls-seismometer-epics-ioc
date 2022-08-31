"""
    @author: André de Oliveira Águila Favoto
    @create: july, 2022
    @title: main
"""
import os
from rawFileMonitor import RawFileMonitor

try:
    fileMonitor = RawFileMonitor()
    fileMonitor.start()
except Exception as e:
    print(f'Error starting up: {e.args[0]}')
    os._exit(1)