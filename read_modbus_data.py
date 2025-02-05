from pymodbus.client.sync import ModbusTcpClient

# Connect to Modbus device (replace IP & port)
client = ModbusTcpClient('192.168.1.100', port=502)

# Read holding register (assuming sensor data is at register 100)
result = client.read_holding_registers(100, 1)
temperature = result.registers[0]  # Read first register

print(f"Temperature: {temperature} °C")

client.close()
