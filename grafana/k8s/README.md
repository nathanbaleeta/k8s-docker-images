#### Use Prometheus in Kubernetes

Start the k8s server locally
```
minikube start --extra-config=apiserver.authorization-mode=RBAC --driver=docker --memory=2048 
```

Apply the manifest to your Kubernetes cluster
```
alias k=kubectl
```
```
kubectl create ns monitoring
kubectl apply -n monitoring -f grafana.yaml
```

##### Use port forwarding to access Grafana web UI
```
kubectl port-forward <grafana-pod> 3000:3000 -n monitoring
```
