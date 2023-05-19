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
    
]

# Define the configuration commands to execute
config_commands = [
    'interface GigabitEthernet0/0',
    'ip address 172.16.3.8 255.255.255.0',
    'no shutdown',
    # Add more configuration commands as needed
]

# Loop through each device and execute the configuration commands
for device in devices:
    try:
        # Establish a connection to the device
        net_connect = ConnectHandler(**device)

        # Print the device IP address
        print(f"Device: {device['ip']}\n")

        # Send configuration commands and print the output
        output = net_connect.send_config_set(config_commands)
        print(f"Configuration Output:\n")
        print(output)
        print("-" * 50)

        # Save the configuration
        save_output = net_connect.save_config()
        print(f"Save Configuration Output:\n")
        print(save_output)
        print("-" * 50)

        # Close the SSH connection
        net_connect.disconnect()

    except Exception as e:
        print(f"Unable to connect to {device['ip']}. Error: {str(e)}")
    finally:
        print("-" * 50)