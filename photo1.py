import requests,hashlib

jelszo = input("jelszot! ")
sha = hashlib.sha512(jelszo.encode("utf-8")).hexdigest()
url = "http://docker.lan:8420/test"
d = {'password': sha}
try:
	valasz = requests.post(url, data = d)
except:
	print("Hiba")
	exit()
a = valasz.status_code
if a == 200:
	print("Jol mukodik")
elif a == 401:
	print("Nem adtal meg jelszot")
elif a == 403:
	print("Nem jo jelszot adtal meg!")
else:
	print("Belso hiba")

