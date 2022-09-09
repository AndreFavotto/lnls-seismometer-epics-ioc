#!/bin/bash

SERVICE_NAME=docker-ioc

export APP_DIR="$PWD"
envsubst < ./template.service.tmpl > ${SERVICE_NAME}.service
cp ./${SERVICE_NAME}.service /etc/systemd/system

systemctl enable ${SERVICE_NAME}.service
systemctl start ${SERVICE_NAME}.service