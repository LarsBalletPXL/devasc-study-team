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
    # Add more devices as needed
]

# Define the show commands to run
show_commands = [
    'show interfaces',
    'show version',
]

# Iterate over each device
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Create a filename for saving the output
    filename = f"{device['ip']}_output.txt"

    # Open a file to save the output
    with open(filename, 'w') as file:
        # Run show commands on the device
        for command in show_commands:
            output = net_connect.send_command(command)

            # Save the output to the file
            file.write(f"Output for {command}:\n{output}\n")
            file.write('-' * 50)
            file.write('\n')

    # Close the SSH connection
    net_connect.disconnect()