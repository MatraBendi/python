import requests
try:
	valasz = requests.get("http://alocalhosta:3000/cars" , timeout=1)
except requests.exceptions.Timeout:
	print("Hiba turelmeteln voltal")
	exit()
#except requests.exceptions.RequestException as error:
#	print("HIBA TORTNET A CSATLAKOZASNAL:")
#	print(str(error))
#	exit()
except requests.exceptions.TooManyRedirects:
	print("rossz url")
except requests.ReadTimeout:
	print("Hiba")
except KeyboardInterrupt:
	print("Someone closed the program")
else:
	print("nincs hiba")
#print(valasz.status_code)
#print(requests.codes.__dict__)
#print(valasz.headers)
#print(valasz.text)
#print(requests.exceptions.__dict__)
