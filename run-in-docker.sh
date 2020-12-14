#!/bin/bash
docker run --rm --mount src=$(pwd),target=/mnt/www,type=bind --workdir=/mnt/www fsl-pages "$@"
