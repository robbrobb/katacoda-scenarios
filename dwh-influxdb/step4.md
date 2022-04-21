For our next step we need to install the relevant python libraries.

```docker exec dwh-influxdb influx auth create --org dwh-org --all-access```{{execute}}



`pip install influxdb-client`{{execute}}   

The python script looks like this:

<pre class="file" data-target="clipboard">
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
</pre>

First we need to import the relevant libraries we just installed.

<pre class="file" data-target="clipboard">
bucket = "<my-bucket>"
org = "<my-org>"
token = "<my-token>"
url="https://us-west-2-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
</pre>

Then we store relevant data about our bucket, organization and token in variables, and use them to instantiate a `influxdb_client`.

<pre class="file" data-target="clipboard">
write_api = client.write_api(write_options=SYNCHRONOUS)
</pre>

The `influxdb_client` has a `write_api` method that can be used to instantiate the writer object. 

<pre class="file" data-target="clipboard">
p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
</pre>

For our last step, we create a `point` object that we then insert into our bucket.

`python3 influxdb2/write_to_influxdb.py`{{execute}} 


The script will now continuously fill data into our bucket. To view our data, once again select the data source in the query builder by filtering the tags as follows: `my_measurement` for `_measurement`, `my_value` for `_field` and `my_location` for `location`. Alternatively you could use below query for the string query editor to achieve the same result.

<pre class="file" data-target="clipboard">
from(bucket: "dwh-data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "my_measurement")
  |> filter(fn: (r) => r["_field"] == "my_value")
  |> filter(fn: (r) => r["location"] == "my_location")
  |> aggregateWindow(every: v.windowPeriod, fn: last, createEmpty: false)
  |> yield(name: "last")
</pre>

The resulting graph should look something like this:

![Data Showcase](./assets/sine-curve.png)