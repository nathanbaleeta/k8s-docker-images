## Building custom Airflow image for K8s


### Build the Docker Image
Provide a suitable tag (e.g., latest or a version number). 
```
docker build -t airflow-custom:latest .
```

### Push the Image to a Registry 
Once built, push the image to your container registry so your Kubernetes cluster can pull it
```
docker push nbaleeta/airflow-custom:latest
```