#### Use Prometheus in Kubernetes

Start the k8s server locally
```
minikube start --extra-config=apiserver.authorization-mode=RBAC
```

Apply the manifest to your Kubernetes cluster

```
kubectl create ns prometheus-monitoring
kubectl apply -n prometheus-monitoring -f prometheus.yaml
```
