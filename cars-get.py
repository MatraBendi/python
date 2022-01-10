import requests
try:
	valasz = requests.get("http://localhost:3000/cars" , timeout=1)
except:
	print("Hiba")
	exit()

print(valasz.status_code)
for idx, item in enumerate(valasz.json()):
    print(f"{idx+1}. {item['brand']}  {item['model']}")
