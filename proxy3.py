import requests

url = "https://postman-echo.com/basic-auth"
user = "postman"
password = "password"

try:
        reply = requests.get(url, auth = (user, password))
except:
        print("Hiba")
        exit()

print(reply.status_code)
print(reply.json())
