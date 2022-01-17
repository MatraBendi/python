import requests
from requests.auth import HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/user/pass'

try:
        valasz = requests.get(url, auth=HTTPDigestAuth("user","pass"))
except:
        print("hiba")
        exit()

print(valasz.status_code)
