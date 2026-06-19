#### Use ClickHouse in [Kubernetes](https://clickhouse.com/blog/clickhouse-kubernetes-operator)

Start the k8s server locally
```
minikube start --extra-config=apiserver.authorization-mode=RBAC --driver=docker --memory=2048 
```

Apply the manifest to your Kubernetes cluster
```
alias k=kubectl
```
