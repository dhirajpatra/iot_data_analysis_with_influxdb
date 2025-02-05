from influxdb import InfluxDBClient
import pandas as pd
import matplotlib.pyplot as plt

client = InfluxDBClient(host='YOUR_INFLUXDB_SERVER', port=8086, database='iotdb')

query = 'SELECT * FROM "temperature_sensor" ORDER BY time DESC LIMIT 100'
result = client.query(query)
data = list(result.get_points())

df = pd.DataFrame(data)
df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize=(10, 5))
plt.plot(df['time'], df['temperature'], label="Temperature (°C)", marker='o')
plt.plot(df['time'], df['humidity'], label="Humidity (%)", marker='s')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Warehouse Temperature & Humidity')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
