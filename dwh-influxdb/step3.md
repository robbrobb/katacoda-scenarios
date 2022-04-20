# Load CSV-Data into InfluxDB

For our next step, we want to load data in a .csv-format into InfluxDB. As our datasource, we are going to use a demo file locatet at `var/lib/influxdb2/test_data_2.csv` inside the InfluxDB docker container and under `/influxdb2/test_data_2.csv` on the virtual machine. The contents look like this:

    #datatype measurement,tag,double,dateTime:RFC3339
    m,host,used_percent,time
    mem,host1,64.23,2022-04-04T00:00:00Z

The first line defines the datatypes used for the different columns. The second line defines the names of the columns, and the following columns are actual data.




```influx write -b dwh-data -f var/lib/influxdb2/test_data_2.csv```{{execute}}