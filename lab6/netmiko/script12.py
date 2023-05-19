from netmiko import ConnectHandler

# Define the device details in a dictionary
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Establish an SSH connection to the device
net_connect = ConnectHandler(**device)

# Send commands to the device based on conditional statements
output = net_connect.send_command('show interfaces')
if 'GigabitEthernet1/0/1' in output:
    print("Interface GigabitEthernet1/0/1 exists on the device.")
elif 'GigabitEthernet1/0/2' in output:
    print("Interface GigabitEthernet1/0/2 exists on the device.")
else:
    print("No matching interfaces found on the device.")

# Close the SSH connection
net_connect.disconnect()