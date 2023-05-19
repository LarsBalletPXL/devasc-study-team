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

# Loop through each device and backup the configuration
for device in devices:
    try:
        # Establish a connection to the device
        net_connect = ConnectHandler(**device)

        # Print the device IP address
        print(f"Device: {device['ip']}\n")

        # Get the device hostname
        hostname = net_connect.send_command('show run | i hostname')
        hostname = hostname.split()[-1]  # Extract the hostname from the output

        # Backup the configuration to a file
        filename = f"{hostname}_config_backup.txt"
        output = net_connect.send_command('show running-config')
        with open(filename, 'w') as backup_file:
            backup_file.write(output)

        # Close the SSH connection
        net_connect.disconnect()

    except Exception as e:
        print(f"Unable to connect to {device['ip']}. Error: {str(e)}")
    finally:
        print("-" * 50)