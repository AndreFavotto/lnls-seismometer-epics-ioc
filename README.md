# EPICS IOC: LE-3D/5s Seismometer

The app runs by monitoring raw files written by the seismometer's recorder (DAS 130-01), converting it to a known format and then writing it to the EPICS PV RR-09S:SS-Seismic-Ax13:S-Mon, where:

RR: Rack Room
09S: 9th Sirius' sector
SS: Stability System
Seism: Seismometer system
Ax13: 13th Sirius' building axis
S-Mon: Speed Monitoring

This application relies on DAS 130-01 file writing system, so the server's path to the files must be mounted on the container.

@authors: André de Oliveira Águila Favoto/ Leonardo Rossi Leão / Rodrigo de Oliveira Neto 
