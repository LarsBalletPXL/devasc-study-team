from netmiko import ConnectHandler
IP_ADDRESS = "172.16.3.2"
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host=IP_ADDRESS,
    port="22",
    username="test",
    password="test"
    )
config_commands = (
    'logging monitor' ,
    )
output=sshCli.send_config_set(config_commands)
output=sshCli.send_command("show logging")
print(output)