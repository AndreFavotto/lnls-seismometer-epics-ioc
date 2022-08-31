"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modify: july, 2022
    @title: File monitor
"""

import os, threading, shutil, datetime
from datFileMonitor import DatFileMonitor

class RawFileMonitor(threading.Thread):
    
    def __init__(self):
        super(RawFileMonitor, self).__init__()
        self.kill = threading.Event()
        self.path_in = '/home/reftek/bin/archive'
        self.path_cvt = self.path_in + '/../pas2asc'
        self.datFileMonitor = DatFileMonitor()
        
    def scanFiles(self):
        today = datetime.datetime.now()
        year = today.year
        dayOfYear = (today - datetime.datetime(year, 1, 1)).days + 1
        filesPath = f'{self.path_in}/{year}{dayOfYear}/B67D/1/'
        arquivos = set(os.listdir(filesPath))
        return (filesPath, arquivos)
    
    def cleanFiles(self):
        try: #delete last month's local files if not deleted yet
            lastMonth = datetime.datetime.now() - datetime.timedelta(days=30)
            lmYear = lastMonth.year
            lmDayOfYear = (lastMonth- datetime.datetime(lmYear, 1, 1)).days + 1
            oldPath = f'{self.path_in}/{lmYear}{lmDayOfYear}'
            shutil.rmtree(oldPath)
        except FileNotFoundError:
            pass

    def convert(self, filesPath, newFiles):
        for file in newFiles:
            path_in = filesPath + file
            if '_00000000' not in path_in: # xxxxxxx_00000000: File is still processing
                os.system(self.path_cvt + ' -Ln ' + path_in)
                os.remove(path_in)
                self.datFileMonitor.run()
        
    def run(self):
        try:
            filesPath, content = self.scanFiles()
            while not self.kill.is_set():
                self.cleanFiles()
                filesPath, newContent = self.scanFiles()
                newFiles = newContent.difference(content)
                # Converts data if new file found
                if newFiles:
                    self.convert(filesPath,newFiles)
                content = newContent
        except Exception as e:
            print(f'Error in raw file monitoring: {e.args[0]}')
            #logger = logging.handlers.RotatingFileHandler()
            os._exit(1)