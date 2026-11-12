##   [Running Kafka server locally using Docker](https://kafka.apache.org/)

#### Run a Kafka container locally
Start a Kafka instance
```
docker run --name some-kafka -d \
  -p 9092:9092 \
  dhi.io/kafka:4
```
