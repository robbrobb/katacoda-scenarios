The environment used for this catacoda (Ubuntu 20.4) already comes with docker preinstalled. We can test the install with the `docker info`{{execute}} command, and test the execution of containers with `docker run hello-world`{{execute}}. This will run a simple demo container displaying a standard message.

For this excercise we are going to be using the official InfluxDB docker image. It can be pulled via the `docker pull influxdb`{{execute}} command.

Next we start an InfluxDB container under the name ```dwh-influxdb```.  
`docker run -d -p 8086:8086 --volume $(pwd)/influxdb2:/var/lib/influxdb2 --name dwh-influxdb influxdb:latest`{{execute}}  
This label can later be used to modify and control the container instance. For istance one could use it to
- access the container shell `docker exec -it dwh-influxdb /bin/sh`{{execute}} (only use this in a second terminal, as otherwise you wont be able to access the first one anymore)
- start the container `docker start dwh-influxdb`{{execute}}
- stop the container `docker stop dwh-influxdb`{{execute}}

The `-p` flag in our run command has exposed the relevant ports of the container to the network. That means we can access the InfluxDB GUI via a webbrowser. After starting the container, his can be done either by using the tab `InfluxDB` or by using this link https://[[HOST_SUBDOMAIN]]-8086-[[KATACODA_HOST]].environments.katacoda.com/.