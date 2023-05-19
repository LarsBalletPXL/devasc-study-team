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

# Define the configuration commands to send
config_commands = [
    'interface GigabitEthernet1/0/1',
    'description Connected to Switch A',
    'no shutdown',
    'exit',
]

# Iterate over each device
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Enter configuration mode on the device
    net_connect.config_mode()

    # Send configuration commands to the device
    output = net_connect.send_config_set(config_commands)
    print(f"Configuration output for {device['ip']}:\n{output}")
    print('-' * 50)

    # Exit configuration mode
    net_connect.exit_config_mode()

    # Save the configuration changes
    net_connect.save_config()

    # Close the SSH connection
    net_connect.disconnect()