import requests

url = "http://postman-echo.com/basic-auth"
user = "postman"
password = "password"
p = {'http': 'http://localhost:8080/', 'https': 'http://localhost:8080/'}

try:
        reply = requests.get(url, auth = (user, password), proxies = p)
except:
        print("Hiba")
        exit()

print(reply.status_code)
print(reply.json())
