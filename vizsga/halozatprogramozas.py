from netmiko import ConnectHandler
from getpass import getpass
s1 = {
        "device_type" : "cisco_ios",
        "host" : "172.19.0.2",
        "username" : "admin",
        "password" : getpass(),


}
sw1 = ConnectHandler(**s1)
valasz = sw1.send_command("vtp password SouthBrokers")
print(valasz)
sw1.disconnect()
