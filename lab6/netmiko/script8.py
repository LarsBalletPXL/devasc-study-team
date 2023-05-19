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

# Define the interface configuration commands
interface_commands = [
    'interface GigabitEthernet0/0',
    'ip address 172.16.3.8 255.255.255.0',
    'no shutdown',
    # Add more interface configuration commands as needed
]

# Loop through each device and configure the interfaces
for device in devices:
    try:
        # Establish a connection to the device
        net_connect = ConnectHandler(**device)

        # Print the device IP address
        print(f"Device: {device['ip']}\n")

        # Send interface configuration commands and print the output
        output = net_connect.send_config_set(interface_commands)
        print(f"Interface Configuration Output:\n")
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