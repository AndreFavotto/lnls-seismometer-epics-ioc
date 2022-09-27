# EPICS IOC: LE-3D/5s Seismometer

The app runs by monitoring raw files written by the seismometer's recorder (DAS 130-01), converting it to a known format and then writing it to an EPICS PV. Currently using RR-09S:SS-Seismic-Ax13:S-Mon, where:

RR: Rack Room
09S: 9th Sirius' sector
SS: Stability System
Seism: Seismometer system
Ax13: 13th Sirius' building axis
S-Mon: Speed Monitoring

## Executing containerized IOC:

In order to run this application inside a docker container, docker engine and docker compose must be installed. The versions used in this application were:

```
Docker version 20.10.17, build 100c701
Docker Compose version v2.6.0
```

Once done, one can do as follows:

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

3. If using docker as container manager, one can add restart policies to `docker-compose.yml` file, then run from project's main directory:

`docker compose up`

## Executing IOC locally:

To start IOC locally (outside container), one must install manually the pcaspy library:

`pip3 install pcaspy`

For this application, pcaspy 0.7.3. was used.

After this, one can run the following line from project's main directory:

`python3 ./scripts/main.py -p [DAS_PATH] -P [PV_PREFIX] -i [UNIT_ID] -s [DATA_STREAM]`

Where:
```
-p P        Path to DAS-130 files (e.g.: /home/reftek/bin)
-P P        Seismometer's PV prefix (e.g.: RR-09S:SS-Seism-Ax13:)
-i I        Unit ID (e.g.: B67D)
-s S        Unit's data stream to hear data (e.g.: 1)
```

@authors: André de Oliveira Águila Favoto/ Leonardo Rossi Leão / Rodrigo de Oliveira Neto 
