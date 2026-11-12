##   [Running Kafka server locally using Docker](https://kafka.apache.org/)

#### Run a Kafka container locally
Start a Kafka instance
```
docker run --name some-kafka -d \
  -p 9092:9092 \
  dhi.io/kafka:4
```

#### Verify and Test the Broker

**Inspect broker logs.** Check the container logs for the startup confirmation message.
```
docker logs kafka | grep -i "started"
```

