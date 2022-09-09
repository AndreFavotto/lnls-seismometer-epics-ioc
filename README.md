# EPICS IOC: LE-3D/5s Seismometer

The app runs by monitoring raw files written by the seismometer's recorder (DAS 130-01), converting it to a known format and then writing it to an EPICS PV. Currently using RR-09S:SS-Seismic-Ax13:S-Mon, where:

RR: Rack Room
09S: 9th Sirius' sector
SS: Stability System
Seism: Seismometer system
Ax13: 13th Sirius' building axis
S-Mon: Speed Monitoring

## Excecuting IOC:

This application runs inside a docker container, so beside DAS's system, docker engine must be installed.

1. Define `.env` attributes:
```
DAS_PATH= #path where DAS has been installed (e.g.: /home/reftek/bin)
PV_PREFIX= #PV prefix before S-Mon: (e.g.: RR-09S:SS-Seism-Ax13:)
UNIT_ID= #DAS unit Identification (e.g.: B67D)
DATA_STREAM= #Unit's Data Stream providing files (e.g.: 1)
```
2. To install IOC as a service and use systemd as manager, run:

`sudo bash ./install.sh`

and the IOC should be UP and running.

@authors: André de Oliveira Águila Favoto/ Leonardo Rossi Leão / Rodrigo de Oliveira Neto 
