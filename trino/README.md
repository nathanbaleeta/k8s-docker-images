## Building custom Trino image for K8s
To build the specific Trino modules (trino-server and trino-cli) and then the associated locally modified Docker image, execute the following commands from the root directory of the Trino project: 

[Trino](https://github.com/trinodb/trino) is a standard Maven project. Simply run the following command from the project root directory:
```
./mvnw clean install -DskipTests
```
To build image for specific released version, specify -r option (may require buildx for building images)
```
build.sh -r 475
```
