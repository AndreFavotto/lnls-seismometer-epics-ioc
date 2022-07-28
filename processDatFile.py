"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modify: july, 2022
    @title: Data processor and publisher
"""
import time
from iocSeismometer import ioc

class ProcessDatFile:
    
    @staticmethod
    def getValue(data):
        option, value = tuple(data.replace(' ','').split('='))
        return value
    
    @staticmethod
    def convertCounts(counts, bitWeight):
        volts = counts * bitWeight
        # Transduction factor: 800 V/(m/s) 
        speed = volts / 800
        return speed
    
    @staticmethod
    def processFile(data, canal):
        ioc_data = ioc() #instantiating IOC object
        data = data.replace('$', '').split('\n')
        bitWeight = float(ProcessDatFile.getValue(data[6]))
        # Seismic Data
        for counts in data[10:(len(data)-1)]:
            value = ProcessDatFile.convertCounts(float(counts), bitWeight)
            ioc_data.write('leitura', value)
            ioc_data.write('canal', canal)
            time.sleep(0.01) #Simulating DAS sampling frequency (100hz)