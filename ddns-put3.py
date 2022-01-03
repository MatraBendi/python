import requests, json

ct_h = {"Content-Type" : "application/json"}
d = {"id": 1,
      "nev": "otthoni",
      "ip": "31.251.53.1",
      "datum": "2022.01.03 14:31:30"}
try:
        valasz = requests.put("http://localhost:3000/ddns/1", data=json.dumps(d), headers = ct_h)
        print(valasz.status_code)
        valasz = requests.get("http://localhost:3000/ddns)
except:
        print("Mas hiba")
print(valasz.text)
