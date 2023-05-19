from netmiko import ConnectHandler

# Define the device details
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Read the configuration file
with open('config_file.txt', 'r') as file:
    config = file.read()

# Establish a connection to the device
net_connect = ConnectHandler(**device)

# Enter configuration mode on the device
net_connect.config_mode()

# Send the configuration to the device
output = net_connect.send_config_set(config)

# Exit configuration mode
net_connect.exit_config_mode()

# Save the configuration changes
net_connect.save_config()

# Close the SSH connection
net_connect.disconnect()