## Building custom Airflow image for K8s


### Build the Docker Image from template Dockerfile
Provide a suitable tag (e.g., latest or a version number). 
```
docker build -t nbaleeta/airflow-custom:latest .
```

### Verify docker image properly built
Airflow image name:tag should match a built image locally available
```
cd scripts && ./verify_docker_image.sh -t nbaleeta/airflow-custom:latest
```

### Push the Image to a Registry 
Once built, push the image to your container registry so your Kubernetes cluster can pull it
```
docker push nbaleeta/airflow-custom:latest
```

