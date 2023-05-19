from netmiko import ConnectHandler

# Define the device details for each device in a list
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.3.1',
        'username': 'test',
        'password': 'test',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.3.2',
        'username': 'test',
        'password': 'test',
    },
    
]

# Iterate over each device
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Send show commands to the device
    commands = ['show interfaces', 'show version']
    for command in commands:
        output = net_connect.send_command(command)
        print(f"Output for {command} on {device['ip']}:\n{output}")
        print('-' * 50)

    # Close the SSH connection
    net_connect.disconnect()