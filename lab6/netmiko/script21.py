from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Establish an SSH connection to the device
net_connect = ConnectHandler(**device)

# Perform actions based on conditions
output = net_connect.send_command('show interfaces')

if 'GigabitEthernet1/0/1' in output:
    print("Interface GigabitEthernet1/0/1 is up")
elif 'GigabitEthernet1/0/2' in output:
    print("Interface GigabitEthernet1/0/2 is up")
else:
    print("No relevant interfaces found in the output")

# Close the SSH connection
net_connect.disconnect()