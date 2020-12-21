#!/bin/bash

fsl_mount=/mnt/fsl

docker run --rm --mount src=$(cd ../; pwd),target=$fsl_mount,type=bind \
                --workdir=$fsl_mount/www -it fsl-pages "$@"
