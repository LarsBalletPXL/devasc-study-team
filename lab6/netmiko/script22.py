from netmiko import ConnectHandler
import datetime

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

# Connect to each device and perform tasks
for device in devices:
    # Establish an SSH connection to the device
    net_connect = ConnectHandler(**device)

    # Retrieve the device hostname and version information
    hostname = net_connect.send_command('show run | i hostname')
    version = net_connect.send_command('show version | i Cisco IOS Software')

    # Retrieve the ARP table
    arp_table = net_connect.send_command('show ip arp')

    # Perform a connectivity test to tftp server
    target_ip = '10.199.64.134'
    ping_output = net_connect.send_command(f'ping {target_ip}')

    # Save the output to separate text files for each device
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{hostname.strip()[9:]}_{current_time}.txt'
    with open(filename, 'w') as file:
        file.write(f'Hostname: {hostname}\n')
        file.write(f'IOS Version: {version}\n')
        file.write('\nARP Table:\n')
        file.write(arp_table)
        file.write('\nConnectivity Test:\n')
        file.write(ping_output)

    # Close the SSH connection
    net_connect.disconnect()