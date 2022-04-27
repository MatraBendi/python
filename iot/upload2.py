url = "http://docker.lan:8888/upload"
try:
        n = 0
        while True:
                temp = random.randint(15,25)
                datum = datetime.now()
                d = {"date":datum,"type":"Temperature","value":temp,"token":token}
                reply = requests.post(url, data = d)
                if reply.status_code == 200:
                        print(d)
                        n += 1
                else:
                        break
                sleep(1)
except KeyboardInterrupt:
        print("")
        print(f"kiirtunk {n} sort")
except:
        print("halozati hiba")
