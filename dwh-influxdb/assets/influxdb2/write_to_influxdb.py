import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "dwh-data"
org = "dwh-org"
token = "<my-token>"
# Store the URL of your InfluxDB instance
url="https://us-west-2-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
