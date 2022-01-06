import requests, json , sys

ip = input("adjon meg egy ip-t: ")

if len(sys.argv) == 1:
	print("Nem adt")
	exit()

szam = sys.argv[1]

if szam ==  sys.argv[1]:
	print("jo szamot adott meg")
else:
	print("Hibas szam (csak 1 lehet vagy 2)")

ct_h = {"Content-Type" : "application/json"}
d = {"id": szam, "nev": "otthoni", "model": ip, "datum": "1988.10.12. 12:00:21"}
try:
        valasz = requests.get("http://localhost:3000/ddns/"+ szam, data=json.dumps(d), headers = ct_h)
        print(valasz.status_code)
#	valasz = requests.put("http://localhost:3000/ddns/" + szam)
except:
        print("Mas hiba")
