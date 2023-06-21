# Starting this App

```bash
# Start the Flask app (Open localhost:5000/companies/)
docker-compose up -d
# start minikube
minikube start
# to push images to minikube registry - local daemon
eval $(minikube docker-env)
docker-compose build
# apply the manifests
kubectl apply -f k8s/deployment-api.yaml
kubectl apply -f k8s/deployment-mysql.yaml
kubectl apply -f k8s/service-api.yam
kubectl apply -f k8s/service-mysql.yaml
# generate service url
minikube service api --url
```
