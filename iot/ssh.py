from netmiko import ConnectHandler
from getpass import getpass

r1 = {
        "device_type" : "cisco_ios",
        "host" : "172.17.0.100",
        "username" : "admin",
        "password" : getpass(),
}

r2 = {
        "device_type" : "cisco_ios",
        "host" : "172.19.0.2",
        "username" : "admin",
        "password" : getpass(),
}

command = "sh ip route"
with ConnectHandler(**r1) as c:
        #output = c.send_command(command)

print(outut)

