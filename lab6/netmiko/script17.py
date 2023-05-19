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

# Define the subset of interfaces to configure
interface_config = {
    'GigabitEthernet1/0/1': {
        'description': 'Connected to Switch A',
        'shutdown': False,
    },
    'GigabitEthernet1/0/2': {
        'description': 'Connected to Switch B',
        'shutdown': True,
    },
}

# Iterate over each device
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Enter configuration mode on the device
    net_connect.config_mode()

    # Configure the interfaces on the device
    for interface, config in interface_config.items():
        commands = [f'interface {interface}']
        for key, value in config.items():
            if isinstance(value, bool):
                value = 'no shutdown' if value else 'shutdown'
            commands.append(f'{key} {value}')
        output = net_connect.send_config_set(commands)
        print(f"Configuration output for {interface} on {device['ip']}:\n{output}")
        print('-' * 50)

    # Exit configuration mode
    net_connect.exit_config_mode()

    # Save the configuration changes
    net_connect.save_config()

    # Close the SSH connection
    net_connect.disconnect()