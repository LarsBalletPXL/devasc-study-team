from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Define list of configuration commands to send
config_commands = [
    'interface gigabitethernet0/2',
    'description Network connection',
    'ip address 192.168.1.10 255.255.255.0',
]

# Establish SSH connection to device
with ConnectHandler(**device) as ssh:

    # Send configuration commands and print output
    output = ssh.send_config_set(config_commands)
    print(f"Output:\n{output}\n")