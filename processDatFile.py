"""
    @authors: Leonardo Rossi Leão / Rodrigo de Oliveira Neto / André de Oliveira Águila Favoto
    @create: november, 24, 2020
    @modify: july, 2022
    @title: Data processor and publisher
"""
import datetime
from iocSeismometer import ioc

class ProcessDatFile:
    
    @staticmethod
    def getValue(data):
        option, value = tuple(data.replace(' ','').split('='))
        return value
    
    @staticmethod
    def processDate(fileDate):
        fileDate = ProcessDatFile.getValue(fileDate)
        year, dayOfYear, hour, minutes, seconds, ms = tuple(fileDate.replace('.', ':').split(':'))
        dt = datetime.date(int(year), 1, 1) + datetime.timedelta(int(dayOfYear) - 1)
        ms = int(ms)/10**6
        return datetime.datetime(dt.year, dt.month, dt.day, int(hour), int(minutes), int(seconds), int(ms))
    
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
        sampleRate = float(ProcessDatFile.getValue(data[3]))
        date = ProcessDatFile.processDate(data[4])
        bitWeight = float(ProcessDatFile.getValue(data[6]))
        # Seismic Data
        for counts in data[10:(len(data)-1)]:
            value = ProcessDatFile.convertCounts(float(counts), bitWeight)
            date = date + datetime.timedelta(milliseconds=(1000/sampleRate))
            ioc_data.write('leitura', value)
            ioc_data.write('canal', canal)