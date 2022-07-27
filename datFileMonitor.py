"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modified: july, 2022
    @title: Data Converter
"""

import os
from processDatFile import ProcessDatFile as pdf    

class DatFileMonitor():
    
    def __init__(self):
        super(DatFileMonitor, self).__init__()
        self.path_in = './'
                        
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
