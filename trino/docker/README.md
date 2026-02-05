##   [Trino](https://trino.io/docs/current/index.html)

#### Run a Trino container locally
The Trino server is now running on localhost:8080 (the default port).
```
docker run -d -p 8080:8080 --name trino trinodb/trino
```

To avoid having to create catalog files and mount them in the container, you can enable dynamic catalog management by setting the CATALOG_MANAGEMENT environmental variable to dynamic.
```
docker run -d -p 8080:8080 --name trino -e CATALOG_MANAGEMENT=dynamic trinodb/trino
```
To make these changes persistent across container restarts, a volume must be mounted at `/etc/trino/catalog`




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
USE catalog.schema
SHOW TABLES;
SHOW COLUMNS FROM table;
```
