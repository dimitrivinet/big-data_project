# toy_server

"""
minikube start

minikube kubectl -- create deployment mongodb --image=mongo

minikube kubectl -- create deployment toy-server --image=dimitrivinet/toy_server

minikube kubectl -- get po -Aw 
"""

wait for toy-server pod to be created and running

"""
minikube kubectl -- expose deployment mongodb --type=NodePort --port=27017

minikube kubectl -- expose deployment toy-server --type=NodePort --port=8080
"""

get toy-server API adress with: 

"""
minikube service toy-server --url
"""

get mongodb adress with: 

"""
minikube service mongodb --url
"""
