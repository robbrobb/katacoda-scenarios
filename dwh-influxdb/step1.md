# Set up Docker environment and containers

The environment used for this catacoda already comes with docker preinstalled. We can test the install with the `docker info`{{execute}} command, and test the execution of containers with `docker run hello-world`{{execute}}. This will run a simple demo container displaying a standard message.

For this excercise we are going to be using the official InfluxDB docker image. It can be pulled via the `docker pull influxdb`{{execute}}.

Next we start an InfluxDB container under the name ```dwh-influxdb```.  
`docker run -d --name dwh-influxdb influxdb:latest`{{execute}}  
This label can later be used to modify and control the container instance. For istance one could use it to
- access the container shell `docker exec -it dwh-influxdb /bin/sh`{{execute}}
- start the container `docker start dwh-influxdb`{{execute}}
- stop the container `docker stop dwh-influxdb`{{execute}}