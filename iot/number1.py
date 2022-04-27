import requests
url = "http://172.16.0.10:8888/number"

try:
        r = requests.get(url)
except:
        print("hiba")
        exit(0)
print(r.status_code)
print(r.json())
