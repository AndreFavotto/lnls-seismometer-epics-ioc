import argparse

class globalVars:

    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser(description='Define environment variables')
        parser.add_argument('-p', required=True, help="Path to DAS-130 files")
        parser.add_argument('-P', required=True, help="Seismometer's PV prefix")
        args = parser.parse_args()
        return args