szov = input("Irjon be egy szamot: ")
def myint(sz):
	n = 0
	for i in sz:
		kod = ord(i)
		if kod >= 48 and kod <=57:
			n = n*10
			n += int(i)
		else:
			return n
	return n
try:
        assert len(szov) >= 1 and len(szov) <= 12
except AssertionError:
        print("Tul nagy vagy tul kicsi a megadott szam")
        exit()

print(myint(szov))
