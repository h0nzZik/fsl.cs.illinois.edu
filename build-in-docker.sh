#!/bin/bash

docker build -t fsl-pages .
./run-in-docker.sh ./build
