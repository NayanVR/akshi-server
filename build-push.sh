#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

DOCKER_USERNAME="nayanvr"
APP_NAME="akshi-server"
TAG="latest" # Update this tag as needed

echo "Compiling requirements.txt from pyproject.toml..."
uv pip compile pyproject.toml -o requirements.txt

IMAGE_NAME="${DOCKER_USERNAME}/${APP_NAME}:${TAG}"
echo "Building & Pushing Docker image: ${IMAGE_NAME}..."
docker buildx build --platform linux/amd64 -t ${IMAGE_NAME} --push .

echo "Docker image ${IMAGE_NAME} has been successfully built and pushed to Docker Hub."
