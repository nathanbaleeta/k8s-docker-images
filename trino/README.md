#### Run a Trino container locally
The Trino server is now running on localhost:8080 (the default port).
```
docker run -d -p 8080:8080 --name trino trinodb/trino
```

#### Run the Trino CLI
Run the Trino CLI, which connects to localhost:8080 by default:
```
docker exec -it trino trino
```

You can pass additional arguments to the Trino CLI to connect to specific catalog/ schema:
```
docker exec -it trino trino --catalog tpch --schema sf1
```

##### Steps to view schemas in a [Trino catalog](https://trino.io/docs/current/sql/use.html)
Identify target catalog
```
SHOW CATALOGS;
SHOW SCHEMAS IN <catalog>; 
SHOW SCHEMAS FROM <catalog>;
USE catalog.schema
SHOW TABLES;
```
