import requests

url = "https://172.16.0.10:5000/bendi"
url2 = "https://172.16.0.10:5000/api/bendi"
user = "bendi"
password = "kakukk"
h = {"Authorization":"Basic cG9zdG1hbjpwYXNzd29yZA=="}
s = requests.Session()
try:
	reply =s.get(url, auth = (user, password))
	d = reply.json()
	t = d['Token']
	reply = s.get(url2, headers={'X-API-Key':'bendi-5'})
except:
	print("Hiba")
	exit()

print(reply.status_code)
print(reply.json())
