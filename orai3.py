import sys

try:
	a = sys.argv[1]
	f = open(a.txt, "rt")
	line = f.readline()
	while line:
		print(line.upper(), end= "")
		line = f.readline()
	f.close()
except:
	print("Hiba!")
