## To verify the version # and mirror site, please visit this link below:
```
https://spark.apache.org/downloads.html?ref=chaosgenius.io
```
#### 1. Download and extract Spark from archive
```
curl -O https://dlcdn.apache.org/spark/spark-4.0.1/spark-4.0.1-bin-hadoop3.tgz
tar -xvf spark-4.0.1-bin-hadoop3.tgz
```

#### 2. Build & push the image to container registry
Spark also ships with a `bin/docker-image-tool.sh` script that can be used to build and publish the Docker images to use with the Kubernetes backend. By default `bin/docker-image-tool.sh` builds docker image for running JVM jobs
```
$ ./bin/docker-image-tool.sh -r nbaleeta -t 4.0.1 build
$ ./bin/docker-image-tool.sh -r nbaleeta -t 4.0.1 push
```

##### To build PySpark docker image
```
$ ./bin/docker-image-tool.sh -r nbaleeta -t 4.0.1 -p ./kubernetes/dockerfiles/spark/bindings/python/Dockerfile build

$ ./bin/docker-image-tool.sh -r nbaleeta -t 4.0.1 -p ./kubernetes/dockerfiles/spark/bindings/python/Dockerfile push
```
