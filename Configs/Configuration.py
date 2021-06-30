from Lib import Connect
try:
    from netmiko import *
except:
    print("Bilinmedik bir hata ile karşılaştık :/")

""""
1. enable
2. configure terminal
3. router rip
4. version 2
5. network...
""""

def RipVersion2():
    config_commands = ['','','']
    output = net_connect.send_config_set(config_commands)
    print(output)

# Tam olarak bitmedi...