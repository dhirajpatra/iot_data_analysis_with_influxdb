from influxdb import InfluxDBClient
import time

# Connect to InfluxDB
influx_client = InfluxDBClient(host='localhost', port=8086, database='iotdb')

# Example sensor data (replace with Modbus read)
temperature = 25.4  

# Format data for InfluxDB
json_body = [
    {
        "measurement": "temperature_sensor",
        "tags": {
            "location": "factory1"
        },
        "fields": {
            "temperature": temperature
        }
    }
]

# Write data to InfluxDB
influx_client.write_points(json_body)
print("Data written to InfluxDB.")
