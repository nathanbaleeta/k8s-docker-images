## Building production ready custom [Trino](https://hub.docker.com/hardened-images/catalog/dhi/trino) image for K8s (Debian based to allow extending)

If you haven't authenticated yet, first run:
```
docker login dhi.io
```
### Build the Docker Image from template Dockerfile
Provide a suitable tag (e.g., latest or a version number). 
```
docker build -t nbaleeta/trino-custom:4.7.9 .
```

### Push the Image to a Registry 
Once built, push the image to your container registry so your Kubernetes cluster can pull it
```
docker push nbaleeta/trino-custom:4.7.9
```
