import requests

valasz = requests.get("http://localhost:3000/cars")
print(valasz.status_code)
#print(requests.codes.__dict__)
#print(valasz.headers)
print(valasz.text)
