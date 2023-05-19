from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.3.2',
    'username': 'test',
    'password': 'test',
}

# Define list of commands to send
commands = ['show interfaces', 'show running-config', 'show ip route']

# Establish SSH connection to device
with ConnectHandler(**device) as ssh:

    # Send each command in turn and print the output
    for command in commands:
        output = ssh.send_command(command)
        print(f"Command: {command}\nOutput:\n{output}\n")