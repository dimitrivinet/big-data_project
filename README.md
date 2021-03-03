# toy_server: a Big Data course project

A simple API to predict flowers of the Iris dataset. It takes a form with 4 values in a POST request and returns a string containing the prediction, while logging the requester's IP, the values provided and the prediction in a mongo database. The API can then be integrated in a Kubernetes minikube cluster and scaled to needs.


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
