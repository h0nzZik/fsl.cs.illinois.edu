#!/bin/bash

set -e

docker build -t fsl-pages .
./run-in-docker.sh ./build
