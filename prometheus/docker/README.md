##   [Running Prometheus locally using Docker](https://prometheus.io/docs/prometheus/latest/getting_started/)

#### Run a Prometheus container locally
The Prometheus server is now running on localhost:9090 (the default port).
```
docker run -d -p 9090:9090 --name prometheus nbaleeta/prometheus-custom:3.12.0-debian13
```
