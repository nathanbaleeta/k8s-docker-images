##   [Running ClickHouse server locally using Docker](https://clickhouse.com/)

#### Run a ClickHouse container locally
The ClickHouse server is now running on localhost:8123 (the default port).
```
docker run -d \
  --name clickhouse-server \
  -p 8123:8123 \
  -p 9000:9000 \
  -e CLICKHOUSE_USER=admin \
  -e CLICKHOUSE_PASSWORD=YourSecurePassword123! \
  nbaleeta/clickhouse-server:25-debian
```

#### Access the UI
Open your browser and navigate to `http://localhost:8123`
