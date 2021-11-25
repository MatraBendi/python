try:
	f = open("/home/bendi/python/filmek.txt", 'rt')
#	print(f.read(50))
#2 fele beolvasaso
	a = f.readline()
	while a:
		print(b, end='')
		a = f.readline()
	f.close()

except:
	print("Nincs meg a fajl")

