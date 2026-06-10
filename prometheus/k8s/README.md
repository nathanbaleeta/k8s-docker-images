#### Use Prometheus in Kubernetes

Start the k8s server locally
```
minikube start --extra-config=apiserver.authorization-mode=RBAC --driver=docker
```

Apply the manifest to your Kubernetes cluster
```
alias k=kubectl
```
```
kubectl create ns prometheus-monitoring
kubectl apply -n prometheus-monitoring -f prometheus.yaml
```
