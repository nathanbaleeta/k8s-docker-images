##   [Running Prometheus locally using Docker](https://grafana.com/)

#### Run a Grafana container locally
The Grafana server is now running on localhost:3000 (the default port).
```
docker run -d -p 3000:3000 nbaleeta/grafana-custom:13-debian-dev
```
