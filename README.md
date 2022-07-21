# Seismometer's EPICS IOC

In order to run this IOC you must be connected to the seismometer's server machine.

Start this application by writing 1 to "start.txt" file and executing main.py (to be modified). The log of activities can be seen at "monitor.txt".

The app runs by monitoring raw files written by the seismometer's recorder, converting it to a known format and then writing it to the EPICS record called LNLS:SISM:.

This IOC is yet to be containerized.