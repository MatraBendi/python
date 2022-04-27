from dotenv import load_dotenv
import os, requests

load_dotenv()
token = os.getenv("API_KEY")
url = "http://docker.lan:8888/fetchAll"
d = {"tabla": "users", "token" : token}
print(d)
try:
        reply = requests.get(url, data=d)
except:
        print("halozati hiba")
        exit()
if reply.status_code == 200:
        print(reply.json())
else:
        print("nincs hitelesitve")
