#!/bin/sh

IMAGE_NAME=arsen3d/audioface_module:latest
DEST_PATH=src/checkpoints

docker pull $IMAGE_NAME
echo "Creating temporary container from $IMAGE_NAME..."
CONTAINER_ID=$(docker create $IMAGE_NAME)

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: Failed to create container"
    exit 1
fi

echo "Copying files from container..."
docker cp $CONTAINER_ID:/app/checkpoints/ $DEST_PATH

echo "Removing temporary container..."
docker rm $CONTAINER_ID

echo "Done!"
