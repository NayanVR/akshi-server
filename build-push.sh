#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

DOCKER_USERNAME="nayanvr"
APP_NAME="akshi-server"
TAG="latest" # Update this tag as needed

echo "Compiling requirements.txt from pyproject.toml..."
uv pip compile pyproject.toml -o requirements.txt

IMAGE_NAME="${DOCKER_USERNAME}/${APP_NAME}:${TAG}"
echo "Building Docker image: ${IMAGE_NAME}..."
docker build -t ${IMAGE_NAME} .

echo "Pushing Docker image to Docker Hub..."
docker push ${IMAGE_NAME}

echo "Docker image ${IMAGE_NAME} has been successfully built and pushed to Docker Hub."
