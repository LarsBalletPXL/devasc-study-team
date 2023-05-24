from netmiko import ConnectHandler

def connect_to_device(device):
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Send commands to the device
    output = net_connect.send_command('show version')
    print(output)

    # Close the SSH connection
    net_connect.disconnect()

# Define the device details in a dictionary
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Call the function to connect to the device
connect_to_device(device)