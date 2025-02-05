# Query temperature data
query = 'SELECT * FROM "temperature_sensor" ORDER BY time DESC LIMIT 10'
result = influx_client.query(query)

# Display data
for point in result.get_points():
    print(f"Time: {point['time']}, Temperature: {point['temperature']} °C")
