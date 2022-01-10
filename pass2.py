import requests

url = "https://postman-echo.com/basic-auth"
#user = "postman"
#password = "password"
h = {"Authorization":"Basic cG9zdG1hbjpwYXNzd29yZA=="}
try:
        reply = requests.get(url, headers = h)
except:
        print("Hiba")
        exit()

print(reply.status_code)
print(reply.json())
