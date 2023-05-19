from netmiko import ConnectHandler

# Define a list of devices with their connection details
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.3.2',
        'username': 'test',
        'password': 'test',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.3.1',
        'username': 'test',
        'password': 'test',
    },
    # Add more devices as needed
]

# Define the show commands to execute
show_commands = ['show version', 'show interfaces', 'show ip route']

# Loop through each device and execute the show commands
for device in devices:
    try:
        # Establish a connection to the device
        net_connect = ConnectHandler(**device)

        # Print the device IP address
        print(f"Device: {device['ip']}\n")

        # Send show commands and print the output
        for command in show_commands:
            output = net_connect.send_command(command)
            print(f"Command: {command}\n")
            print(output)
            print("-" * 50)

        # Close the SSH connection
        net_connect.disconnect()

    except Exception as e:
        print(f"Unable to connect to {device['ip']}. Error: {str(e)}")
    finally:
        print("-" * 50)