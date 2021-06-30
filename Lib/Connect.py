from netmiko import ConnectHandler
import sys

def ConnectToDevice():
    cisco_881 = {
        'device_type' : 'cisco_ios',
        'host' : Host,
        'username' : Username,
        'password' : Password,
        'port' : 8022,
        'secret' : 'secret',
    }
    net_connect = ConnectHandler(**cisco_881)

def InformationsThenSetup():
    global Host,Username,Password
    Host = input("Host adresinizi giriniz : ")
    Username = input("Kullanıcı adınızı giriniz : ")
    Password = input("Şifrenizi giriniz : ")
def Necessery():
    SerialSetup = input("Serial bağlantılarınız kurulu mu (e/h) : ")
    if(SerialSetup == "e"):
        SwitchSetup = input("Switch bağlantılarınız kurulumu (Switch, bilgisayarlar ve Yönlendiricilerle bağlantılı olmalı !) (e/h) : ")
        if(SwitchSetup == "e"):
            PcSetup = input("Bilgisayarlar kurulu mu (e/h) : ")
            if(PcSetup == "e"):
                # PC : Okey | Switch : Okey | Router : Okey
                ConnectToDevice()
    else:
        print("Önce kurulumlarınızı yapınız !")
        sys.exit()

# Tam olarak bitmedi...