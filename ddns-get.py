import requests, json , sys

#sys.argv[] -> ["ddns-get.py", "3"]
if len(sys.argv) == 1:
	print("hasznalat: ddns-get.py <szam 1 es 3 kozott>")
	exit()
szam = int(sys.argv[1])
if szam < 1 or szam >3 :
	print("Hibas szam: csak 1 es 3 kozott lehet")
	exit()
try:
        valasz = requests.get(f"http://localhost:3000/ddns/{szam}")
except:
	print("Hiba!")
	exit()
print(valasz.text)
