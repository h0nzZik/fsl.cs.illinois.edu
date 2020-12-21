#!/bin/bash

set -e
fsl_mount=/mnt/fsl

usage() {
    echo "TODO: Usage message"
}

fatal() {
    echo >&2 "$@"
    usage
    exit 1
}

dockerrun() {
    docker run --rm --mount src=$(cd ../; pwd),target=$fsl_mount,type=bind \
           --workdir=$fsl_mount/www -it fsl-pages "$@"
}

command=$1
shift || fatal "No command specified."

case $command in
    help)  usage ; exit 0 ;;
    image) docker build -t fsl-pages . ;;
    build) dockerrun "./build" ;;
    bash)  dockerrun "bash" ;;
    *)     fatal "Bad command '$command'"; exit 1;;
esac
