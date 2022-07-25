"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modify: july, 2022
    @title: File monitor
"""

import os, threading
from datetime import datetime
from datFileMonitor import DatFileMonitor

class RawFileMonitor(threading.Thread):
    
    def __init__(self):
        super(RawFileMonitor, self).__init__()
        self.kill = threading.Event()
        self.path_in = '/home/reftek/bin/archive'
        self.path_cvt = self.path_in + '/../pas2asc'
        self.datFileMonitor = DatFileMonitor()
        
    def searchFiles(self):
        today = datetime.now()
        year = today.year
        dayOfYear = (today - datetime(year, 1, 1)).days + 1
        path = f'{self.path_in}/{year}{dayOfYear}/B67D/1/'
        arquivos = set(os.listdir(path))
        return (path, arquivos)
    
    def conversao(self, path, newFiles):
        for file in newFiles:
            path_in = path + file
            if '_00000000' not in path_in: # xxxxxxx_00000000: File is still processing
                os.system(self.path_cvt + ' -Ln ' + path_in)
                os.remove(path_in)
                os.system('clear')
                self.datFileMonitor.run()
        
    def run(self):
        path, content = self.searchFiles()
        while not self.kill.is_set():
            path, newContent = self.searchFiles()
            newFiles = newContent.difference(content)
            # Converts data if new file found
            if newFiles:
                self.conversao(path, newFiles)
            content = newContent