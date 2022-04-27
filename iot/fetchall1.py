import requests

url = "http://172.16.0.10:8888/fetchAll"
d1 = {'table':'users','token':'KjwX7-QXRh70JA'}
d2 = {'table':'measurement','token':'KjwX7-QXRh70JA'}
try:
        reply = requests.get(url, data = d1)
except:
        print("Hiba")
        exit()
print(reply.status_code)
print(reply.json())
