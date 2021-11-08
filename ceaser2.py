
bekert = input("Adjon meg egy szoveget! ")

try:
	bekertszam = int(input("Adjon meg egy szamot! "))
	assert bekertszam >=1 and bekertszam <=25
except ValueError:
	print("Nem szamot adtal meg!")
	exit(0)
except:
	print("Hibas szamot adott meg (1-25)")
	exit(0)

for i in bekert:
	kod = ord(i)
	if kod>= 97 and kod <= 122:
		kod += bekertszam
		if kod > 122:
			kod -= 26
		print(chr(kod), end = "")
	elif kod >= 65 and kod <=90:
		kod += bekertszam
		if kod > 90:
			kod -=26
		print(chr(kod), end="")
	else:
		print("Hibas kod!")
print("")
