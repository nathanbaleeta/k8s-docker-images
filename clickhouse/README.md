## Building production ready custom [ClickHouse](https://hub.docker.com/hardened-images/catalog/dhi/clickhouse-server) image for K8s (Debian based to allow extending)

If you haven't authenticated yet, first run:
```
docker login dhi.io
```
### Build the Docker Image from template Dockerfile
Provide a suitable tag (e.g., latest or a version number). 
```
docker build -t nbaleeta/clickhouse-server-custom:25-debian-dev .
```

### Push the Image to a Registry 
Once built, push the image to your container registry so your Kubernetes cluster can pull it
```
docker push nbaleeta/clickhouse-server-custom:25-debian-dev
```
