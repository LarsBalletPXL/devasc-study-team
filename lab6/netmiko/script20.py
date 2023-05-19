from netmiko import ConnectHandler

def execute_script(device):
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Perform actions on the device
    # Example: Send show commands
    output = net_connect.send_command('show interfaces')
    print(output)

    # Close the SSH connection
    net_connect.disconnect()

# Define the device details
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Call the function to execute the script
execute_script(device)