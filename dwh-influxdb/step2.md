We now have to set up the InfluxDB instance. Inside the web GUI, we are firstly prompted to create a local user account, an organisation and a initial bucket. The account is used to login into the web instance. An organization is a workspace for a group of users, which enables access-control for time series data, dashboards, and other resources. A bucket is where your time series data is stored.

![User Setup](./assets/user-setup.png)

For this example we choose
- `admin` as our username
- `password` as our password
- `dwh-org` as our organisation
- and `dwh-data` as our initial bucket name

On the next page choose the "Configure Later" option, since we will configure all things later.

As an alternative to the GUI setup, we can also do all of this by interacting with the docker container in the shell. ```docker exec dwh-influxdb influx setup --bucket dwh-data --org dwh-org --password password --username admin --force```{{execute}}
The `docker exec dwh-influxdb` part of our command causes the rest of the command to be executed inside our container shell. That is where we actually want to set all the variables.
