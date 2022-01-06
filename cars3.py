import requests
import showw_cars

try:
#        ct_h = ("Content-type" : "application/json")
        valasz = requests.post("http://localhost:3000/cars", data= {"id": 2,"brand": "Chevrolet","model": "Camaro", "production_year": 1988,"convertible": T} )
        print(valasz.status_code)
        valasz = requests.put("http://localhost:3000/cars", data= {"id": 3,"brand": "Aston Martin","model": "Rapide", "production_year": 2020,"convertible": F})
         print(valasz.status_code)
        valasz = requests.delete("http://localhost:3000/cars/6")
         print(valasz.status_code)
        valasz = requests.get("http://localhost:3000/cars", timeout = 1)
except requests.exceptions.Timeout as time:
        print("Hiba, turelmetlen voltal", time)
        exit()
except requests.exception as e:
        print("HTTP Error", httpe)
        exit()
except requests.exceptions.ConnectionError as conn:
        print("Connection Error:", conn)
        exit()
except requests.exceptions.RequestException as req:
        print("RequestException Error", req)
        exit()
except:
        print("Mas hiba")
else:
        print("Nincs hiba")
finally:
        print("mindig lefut ag")
