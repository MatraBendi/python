import requests
import json
url = "http://172.16.0.10:8888/regist"
d = {'username' : 'bendi'}
try:
        r = requests.post(url, data = d)
except:
        print("hiba")
        exit(0)
print(r.status_code)
token = json.loads(r.json())['token']
print(token)
with open (".env", "wt") as f:
	f.write(f"API_KEY={token}")
