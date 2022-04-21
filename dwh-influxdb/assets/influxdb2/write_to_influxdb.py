import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import math
import time

bucket = "dwh-data"
org = "dwh-org"
token = ""  #copy the saved token here
url = ""      #copy the InfluxDB-url here

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org    
)

write_api = client.write_api(write_options=SYNCHRONOUS)


while True:

    val = math.sin(time.time()/15) * 10

    p = influxdb_client.Point("my_measurement").tag("location", "my_location").field("my_value", val)
    write_api.write(bucket=bucket, org=org, record=p)

    time.sleep(1)