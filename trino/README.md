## Building custom Trino image for K8s
To build an image for a locally modified version of Trino, run the Maven build (usually takes a while for first time) before building the image

[Trino](https://github.com/trinodb/trino) is a standard Maven project. Simply run the following command from the project root directory:
```
./mvnw clean install -DskipTests
```

```
build.sh
```

To build image for specific released version, specify -r option
```
build.sh -r 381
```
