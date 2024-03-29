# Kubernetes (k8s) example
This repository has the basic scripts to deploy applications on kubernetes (k8s)

## Build
```shell script
docker build -t sergiogq/flask_app:0.1 .
```

## Run
```shell script
docker run -d -p 5000:5000 sergiogq/flask_app:0.1
```
or
```shell script
docker-compose up -d
```

## Push
```shell script
docker push sergiogq/flask_app:0.1
```

## Deploy on Kubernetes

```shell script
kubectl apply -f ./k8s/
```

```shell script
kubectl delete -f ./k8s/
```

### Blog
https://sergioalbertogq.blogspot.com/2019/10/deploying-applications-on-k8s.html
