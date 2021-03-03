# toy_server

### Requirements:

- minikube: https://minikube.sigs.k8s.io/docs/start/


### Usage:

Start and setup:

```bash

minikube start
minikube kubectl -- create deployment mongodb --image=mongo
minikube kubectl -- create deployment toy-server --image=dimitrivinet/toy_server
minikube kubectl -- get po -Aw 

```

Wait for toy-server pod to be created and running.

Expose deployments:

```bash

minikube kubectl -- expose deployment mongodb --type=NodePort --port=27017
minikube kubectl -- expose deployment toy-server --type=NodePort --port=8080

```

Get toy-server API adress with: 

```bash

minikube service toy-server --url

```

Get mongodb adress with: 

```bash

minikube service mongodb --url

```
