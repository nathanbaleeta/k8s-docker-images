### Step-by-Step Commands to run Airflow services:

#### Postgres first
```
make postgres
```
#### Initialize Airflow (migrate database and create the admin user):
```
make init
```
#### Start all services
```
make up
```
#### Open your browser at:
Login credentials: admin, Password: admin
```
http://localhost:8085 (port selected)
```
