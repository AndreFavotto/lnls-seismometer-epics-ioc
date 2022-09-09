#!/bin/bash

SERVICE_NAME=docker-ioc

export APP_DIR="$PWD"
envsubst < ./template.service.tmpl > /etc/systemd/system/${SERVICE_NAME}.service

systemctl enable ${SERVICE_NAME}.service
systemctl start ${SERVICE_NAME}.service