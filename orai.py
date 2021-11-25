import os
bekert = input("Adjon meg egy fajlnevet ")
try:
	r = open(bekert, 'w+')
	f = open('file.txt', 'r+')
except:
	print("Fajl megniytasa nem sikerult")
	exit()
for line in f.readlines():
	r.writelines(line.lower())
	print(line.lower())
f.close()
r.close()
