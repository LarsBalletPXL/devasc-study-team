from netmiko import ConnectHandler

# Define a list of devices with their connection details
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

# Define the show commands to execute
show_commands = ['show version', 'show interfaces', 'show ip route']

# Loop through each device and execute the show commands
for device in devices:
    try:
        # Establish a connection to the device
        net_connect = ConnectHandler(**device)

        # Print the device IP address
        print(f"Device: {device['ip']}\n")

        # Create a file to save the output
        filename = f"{device['ip']}_output.txt"
        output_file = open(filename, 'w')

        # Send show commands and save the output to the file
        for command in show_commands:
            output = net_connect.send_command(command)
            output_file.write(f"Command: {command}\n")
            output_file.write(output)
            output_file.write("\n" + "-" * 50 + "\n")

        # Close the file
        output_file.close()

        # Close the SSH connection
        net_connect.disconnect()

    except Exception as e:
        print(f"Unable to connect to {device['ip']}. Error: {str(e)}")
    finally:
        print("-" * 50)