"""
    @author: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modify: july, 2022
    @title: File monitor
"""

import os, time, threading
from datetime import datetime
from datFileMonitor import DatFileMonitor

class RawFileMonitor(threading.Thread):
    
    def __init__(self):
        super(RawFileMonitor, self).__init__()
        self.kill = threading.Event()
        self.path_in = "/home/reftek/bin/archive"
        self.path_cvt = self.path_in + "/../pas2asc"
        self.datFileMonitor = DatFileMonitor()
        
    def getDateTime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
        
    def recordAction(self, text):
        monitor = open("monitor.txt", "a")
        monitor.write(text + "\n")
        monitor.close()        
        
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
            if "_00000000" not in path_in: # xxxxxxx_00000000: File is still processing
                os.system(self.path_cvt + " -Ln " + path_in)
                os.remove(path_in)
                self.recordAction(f'[{self.getDateTime()}] Action: raw file converted to dat') 
                self.datFileMonitor.run()
        
    def run(self):
        self.recordAction(f'[{self.getDateTime()}] Action: started raw file monitor')
        path, content = self.searchFiles()
        while not self.kill.is_set():
            path, newContent = self.searchFiles()
            newFiles = newContent.difference(content)
            # Caso identificado um novo arquivo na pasta, realiza a conversao
            if newFiles:
                self.recordAction(f'[{self.getDateTime()}] Action: new raw file found')
                self.conversao(path, newFiles)
            content = newContent
            time.sleep(0.5)
