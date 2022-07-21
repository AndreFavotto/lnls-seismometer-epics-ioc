# EPICS IOC: LE-3D/5s Seismometer

In order to run the application you must be connected to the seismometer's server machine.

Start by writing 1 to "start.txt" file and executing main.py (to be modified). The log of activities can be seen at "monitor.txt".

The app runs by monitoring raw files written by the seismometer's recorder (DAS 130-01), converting it to a known format and then writing it to the EPICS record LNLS:SISM:.

This IOC is yet to be containerized.