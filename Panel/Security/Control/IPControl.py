import json
from typing import Counter
import requests
import time

#Path
acl_path = "./Security/Json/AccessControlList.json"
danger_value = False
filter_value = False
safe_value = False

# Lists
safe_1 = []
danger_1 = []
filter_1 = []

# Counters
safe_counter = 0
danger_counter = 0
filter_counter = 0

# Users's IP Address
ip_info = requests.get("https://ipinfo.io/")
ip_info_data = ip_info.json()

with open(acl_path) as f:
    ip_data = json.load(f)
    len_danger = len(ip_data['danger'])
    len_filter = len(ip_data['filter'])
    len_safe = len(ip_data['safe'])

# Danger Control
while(danger_counter < len_danger):
    danger_ip = ip_data['danger'][danger_counter]['ip']
    if ip_info_data['ip'] == danger_ip:
        danger_value = True
    danger_counter+=1

# Safe Control
while(safe_counter < len_safe):
    safe_ip = ip_data['safe'][safe_counter]['ip']
    if ip_info_data['ip'] == safe_ip:
        safe_value = True
    safe_counter+=1

#Filter Control
while(filter_counter < len_filter):
    filter_ip = ip_data['filter'][filter_counter]['ip']
    if ip_info_data['ip'] == filter_ip:
        filter_value = True
    filter_counter+=1
    
def Hammer():
    if(danger_value == True):
        return True
    elif(filter_value == True):
        return "Filter"
    else:
        return "Güvenli"