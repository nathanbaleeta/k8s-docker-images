#!/bin/bash
IMAGE_NAME="airflow-custom:latest"

echo "Verifying Airflow version..."
AIRFLOW_VERSION=$(docker run --rm "$IMAGE_NAME" airflow version)
if [ $? -eq 0 ]; then
    echo "Airflow version found: $AIRFLOW_VERSION"
else
    echo "Failed to get Airflow version."
    exit 1
fi


