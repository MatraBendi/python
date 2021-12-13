import requests
bekert = input("")
try:
	valasz = requests.get(bekert)
except requests.ConnectionError:
	print("haba")
print(valasz.text)
