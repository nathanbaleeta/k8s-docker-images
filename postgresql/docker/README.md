##   [Running PostgreSQL server locally using Docker](https://www.postgresql.org/)

#### Run a PostgreSQL container locally
The PostgreSQL server is now running on localhost:5432 (the default port).
```
docker run --name my-postgres \
    -e POSTGRESQL_PORT=5432 \
    -e POSTGRESQL_DB=mydb \
    -e POSTGRESQL_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -d nbaleeta/postgres-custom:18-debian
```

#### Access the CLI and execute some queries to interact with database
```
docker exec -it my-postgres psql -U postgres
```

##### Show databases
```
\l
```

