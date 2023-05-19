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

# Read the configuration from an external file
with open('config.txt', 'r') as file:
    config_lines = file.readlines()
    config_commands = [line.strip() for line in config_lines if line.strip()]

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