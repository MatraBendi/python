
szoveg = input("Kerem adjon megy egy szoveget: ")

try:
	bekert = int(input("Adja meg az eltolas erteket: "))
	assert bekert >= 1 and bekert <= 25
except ValueError:
	print("Nem szamot adtal meg")
	exit()
except:
	print(" A szam 1 es 25 kozott lehet ")


for i in szoveg:
	kod = ord(i)
	if kod >= 97 and kod <= 122:
		kod += bekert
		if kod > 122:
			kod -= 26
		print(chr(kod), end=" ")
	
	elif kod >= 65 and kod <= 90:
		kod += bekert
		if kod > 90:
			kod -= 26
		print(chr(kod), end=" ")
	else:
		print("Hibas szam")
print("")
