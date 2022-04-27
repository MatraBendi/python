import requests, sys
url = "http://docker.lan:8888/fetch"
szam = sys.argv[1]
d = {"id":szam}
try:
        reply = requests.get(url, data = d)
except:
        print ("Halozati hiba.")
        exit()
if reply.status_code == 200:
        print (reply.json())
else:
        print ("Nincs adat.")
