

szov = input("Irjon be egy szoveget ")
try:
	x = int(input("irjon be egy szamot: " ))
	assert x >= 1 and x <= 25
except ValuError:
	print("Nem szamot adtal meg")
	exit()
except:
	print("Hibas szamot adott meg (1-25)")
	exit()

def alma():
	if x == 1:
		print("\n1el lett eltolva")

for i in szov:
	code = ord(i)
	if code >= 97 and code <= 122:
		code += x
		if code > 122:
			code -= 26
		print(chr(code) , end = "")
	elif code >= 65 and code <= 90:
		code += x
		if code > 90:
			code -= 26
		print(chr(code), end = "")
	else:
		print(i, end = "")

alma()
print("")
