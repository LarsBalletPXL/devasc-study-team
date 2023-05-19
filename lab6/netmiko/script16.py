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

# Iterate over each device
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Get the device hostname
    hostname = net_connect.send_command('show run | i hostname')
    hostname = hostname.split(' ')[-1].strip()

    # Backup the device configuration
    output = net_connect.send_command('show running-config')

    # Create a filename for saving the backup
    filename = f"{hostname}_backup.txt"

    # Save the backup to a file
    with open(filename, 'w') as file:
        file.write(output)

    # Close the SSH connection
    net_connect.disconnect()