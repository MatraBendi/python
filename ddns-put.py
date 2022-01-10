import requests, json , sys

if len(sys.argv) == 1:
	print("Hasznalat: ddns-get.py <szam 1-3 kozott>")
	exit()
szam = int(sys.argv[1])
if szam < 1 or szam > 3:
	print("Hibas szam 1-3ig lehet")
	exit()
ip = input("adjon meg egy ip-t: ")
ct_h = {"Content-Type" : "application/json"}
d = {"id": szam, "nev": "otthoni", "model": ip, "datum": "1988.10.12. 12:00:21"}
try:
        valasz = requests.put(f"http://localhost:3000/ddns/{szam}", data=json.dumps(d), headers = ct_h)
        print(valasz.status_code)

except:
        print("Mas hiba")

