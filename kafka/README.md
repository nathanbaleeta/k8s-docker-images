##   [Running Kafka server locally using Docker](https://kafka.apache.org/)

### Run a Kafka container locally
Start a Kafka instance
```
docker run --name some-kafka -d \
  -p 9092:9092 \
  dhi.io/kafka:4
```

### Verify and Test the Broker
- **Check container status.** Run docker ps to verify the container is up and port 9092 is mapped.
```
docker ps
```

- **Inspect broker logs.** Check the container logs for the startup confirmation message.
```
docker logs kafka | grep -i "started"
```

- **Verify cluster metadata.** Use the cluster script 
```
docker exec -it some-kafka /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server localhost:9092
```

### Test End-to-End Message Flow
Once the broker is confirmed healthy, run an end-to-end test by creating a topic, producing messages, and reading them back.
- **Create a test topic**
  ```
  docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --topic test-topic
  ```
- **List topics to confirm creation**. Verify that `test-topic` appears in the broker's topic list.
  ```
  docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --list
  ```
