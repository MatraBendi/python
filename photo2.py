import requests,hashlib,os

kep = "tumblr_ph8wfjrTSx1s3iw4r_1280.jpg"
jelszo = input("jelszot! ")
meret = os.path.getsize(kep)
sha = hashlib.sha512(jelszo.encode("utf-8")).hexdigest()
url = "http://docker.lan:8420/"
d = {'password': sha, 'filesize' : meret}
try:
	f = open(kep, 'rb')
	valasz = requests.post(url, data = d, files = {'upfile' : f})
	f.close()
except:
	print("Hiba")
	exit()
a = valasz.status_code
if a == 200:
	print("Jol mukodik")
#jelszo az kakukk
elif a == 401:
	print("Nem adtal meg jelszot")
elif a == 403:
	print("Nem jo jelszot adtal meg!")
elif a == 400:
	print("a kliens nem adott meg fajlmeretet")
elif a == 409:
	print("mar letezik a fajl")
elif a == 411:
	print("Rosszul lett megadva a meret")
else:
	print("Belso hiba")

