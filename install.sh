#!/bin/bash

SERVICE_NAME=docker-ioc

export APP_DIR="$PWD"

if envsubst < ./template.service.tmpl > /etc/systemd/system/${SERVICE_NAME}.service
then
    systemctl enable ${SERVICE_NAME}.service
    systemctl start ${SERVICE_NAME}.service
    echo "Created and started ${SERVICE_NAME}.service"
else
    echo "Failed to create ${SERVICE_NAME}.service"
fi