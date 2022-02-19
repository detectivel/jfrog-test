import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "sysinfo")
pinger = requests.get(BASE + "pinger")
print(response.json())
print(pinger.json())