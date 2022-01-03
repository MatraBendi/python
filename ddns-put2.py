import requests
import show_cars
import json

try:
        ct_h = {"Content-Type" : "application/json"}
        valasz = requests.post("http://localhost:3000/cars", data= json.dumps({"id": 10,"brand": "Ford","model": "Focus","production_year": 1998,"convertible": False}, headers = ct_h)
        print(valasz.status_code)
        valasz = requests.put("http://localhost:3000/cars/3", data= {"id": 3,"brand": "Aston Martin","model": "Rapide","production_year": 2020,"convertible": False}, headers = ct_h)
        print(valasz.status_code)
        valasz = requests.delete("http://localhost:3000/cars/6%22)
        print(valasz.status_code)
        valasz = requests.get("http://localhost:3000/cars", timeout = 1)
        print(valasz.status_code)
except requests.exceptions.Timeout as time:
        print("Hiba, turelmetlen voltal!", time)
        exit()
except requests.exceptions.HTTPError as httpe:
        print("HTTP Error: ", httpe)
        exit()
except requests.exceptions.ConnectionError as conn:
        print("Connection Error: ", conn)
        exit()
except requests.exceptions.RequestException as req:
        print("RequestException Error: ", req)
        exit()
except:
        print("Mas hiba")
else:
        print("Nincs hiba")
