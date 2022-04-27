from dotenv import load_dotenv
from datetime import datetime
from time import sleep
import os, requests
load_dotenv()
token = os.getenv("API_KEY")
url = "http://docker.lan:8888/upload"
datum = datetime.now()
d = {"date":datum,"type":"Temperature","value":"20","token":token}
try:
	n = 0
	while True:
		reply = requests.post(url, data = d)
		if reply.status_code == 200:
			print("kiiras")
			n += 1
		else:
			break
		sleep(1)
except KeyboardInterrupt:
	print("")
	print(f"kiirtunk {n} sort")
except:
	print("halozati hiba")
