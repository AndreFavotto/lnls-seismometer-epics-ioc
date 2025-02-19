FROM public.ecr.aws/debian/debian:10-slim

ENV TZ="America/Sao_Paulo"

USER root
#Basic tools
RUN set -e; set -x;\
    mkdir -p ./opt;\
    apt update -y;\
    apt install -y\
    build-essential\
    libreadline-dev\
    wget\
    swig\
    python3\
    python3-pip

# EPICS environment variables
ENV EPICS_VERSION 3.16.2
ENV EPICS_HOST_ARCH linux-x86_64
ENV EPICS_BASE /opt/epics-${EPICS_VERSION}/base
ENV PATH ${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

# EPICS install
RUN set -e; set -x;\
    mkdir -p ./opt/epics-${EPICS_VERSION};\
    cd /opt/epics-${EPICS_VERSION};\
    wget https://epics.anl.gov/download/base/base-${EPICS_VERSION}.tar.gz;\
    tar -zxf base-${EPICS_VERSION}.tar.gz;\
    rm -v base-${EPICS_VERSION}.tar.gz;\
    mv base-${EPICS_VERSION} base;\
    cd base;\
    make -j$(nproc)

RUN pip3 install --upgrade setuptools;\
    pip3 install pcaspy;\
    chmod 777 /opt
    #Chmod was necessary to allow the application to write files.

ARG DAS_PATH
ARG PV_PREFIX
ARG UNIT_ID
ARG DATA_STREAM

ENV DAS_PATH ${DAS_PATH}
ENV PV_PREFIX ${PV_PREFIX}
ENV UNIT_ID ${UNIT_ID}
ENV DATA_STREAM ${DATA_STREAM}

WORKDIR /opt

COPY . .

CMD python3 ./scripts/main.py -p ${DAS_PATH} -P ${PV_PREFIX} -i ${UNIT_ID} -s ${DATA_STREAM} 