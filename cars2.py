import requests
try:
	valasz = requests.get("http://localhost:3000/cars" , timeout=1)
except requests.exceptions.Timeout:
	print("Hiba turelmeteln voltal")
	exit()
except:
	print("mas hiba")
	exit()
print(valasz.status_code)
#print(requests.codes.__dict__)
#print(valasz.headers)
print(valasz.text)
print(requests.exceptions.__dict__)
