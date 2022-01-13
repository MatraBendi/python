import requests

s = requests.Session()

try:
	s.get('https://httpbin.org/cookies/set/sessioncookie/0327')
	s.auth = ('user', 'pass')
	s.headers.update({'x-test': 'true'})
	reply = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
except:
	print("Hiba")
	exit()
print(reply.text)
print(s)

