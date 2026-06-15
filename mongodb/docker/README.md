##   [Running Trino locally using Docker](https://trino.io/docs/current/index.html)

#### Run a Mongo container locally
```
docker run -d --name mongodb -v mongodb_data:/data/db \
  dhi.io/mongodb:8-debian-dev
```

To make these changes persistent across container restarts, a volume must be mounted at `/data/db`


#### Run the Mongodb shell or CLI
Run the MongoDB shell:
```
docker exec -it <mongodb_container_id> mongosh
```

##### Steps to view databases in a [Mongo](https://www.mongodb.com/docs/mongodb-shell/run-commands/)
List databases
```
show dbs
```
