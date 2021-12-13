import requests
import show_cars
valasz = requests.get("http://localhost:3000/ddns?_sort=brand&_order=desc%22")
#print(valasz.status_code)
#print(requests.codes.__dict__)
#print(valasz.headers)
#print(valasz.text)
show_cars.show(valasz.json())
