"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modified: july, 2022
    @title: Data Converter
"""

# Libraries
import os
from datetime import datetime
from processDatFile import ProcessDatFile as pdf    

class DatFileMonitor():
    
    def __init__(self):
        super(DatFileMonitor, self).__init__()
        self.path_in = '/home/reftek/ioc/lnls-seismometer-epics-ioc/'
        
    def getDateTime(self):
        now = datetime.now()
        return now.strftime('%d/%m/%Y %H:%M:%S')
        
    def recordAction(self, text):
        monitor = open('monitor.txt', 'a')
        monitor.write(text + '\n')
        monitor.close()
        
    def searchFiles(self):
        arquivos = set(os.listdir(self.path_in))
        return arquivos
                
    def run(self):
        content = self.searchFiles()
        for filename in content:
            if '.atr' in filename:
                file = open(self.path_in + filename, 'r')
                data = file.read()
                file.close()
                pdf.processFile(data, filename[-5])
                os.remove(self.path_in + filename)
                self.recordAction(f'[{self.getDateTime()}] Action: Channel {filename[-5]} | dat file treatment concluded')

        
