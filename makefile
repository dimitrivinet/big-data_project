build:
	sudo docker build -t dimitrivinet/toy_server .

run:
	sudo docker run -it -p 8080:8080 --expose 27017 dimitrivinet/toy_server