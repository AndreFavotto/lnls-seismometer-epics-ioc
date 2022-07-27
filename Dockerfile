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
ENV EPICS_BASE /opt/epics-3.16.2/base
ENV PATH ${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

# EPICS install
RUN set -e; set -x;\
    mkdir -p ./opt/epics-3.16.2;\
    cd /opt/epics-3.16.2;\
    wget https://epics.anl.gov/download/base/base-3.16.2.tar.gz;\
    tar -zxf base-3.16.2.tar.gz;\
    rm -v base-3.16.2.tar.gz;\
    mv base-3.16.2 base;\
    cd base;\
    make -j$(nproc)

RUN pip3 install --upgrade setuptools;\
    pip3 install pcaspy;\
    chmod 777 /opt
    #Chmod was necessary to allow the application to write files.

WORKDIR /opt

COPY . .

CMD ["python3", "main.py"]