bekert = input("Add meg a fajl nevet: ")
try:
        olvasas = open((bekert), 'r')
        iras = open((bekert + "-out.txt"), 'wt')
except:
	print("Hibas a megadott fajl")
	exit()
be = olvasas.readline()
szamolo = 0
while be:
        szoveg = ""
        if szamolo % 2 != 0:
                szoveg += be.lower()
        else:
                szoveg += be.upper()
        szamolo += 1
        iras.write(szoveg)
        print(szoveg, end="")
        be = olvasas.readline()
olvasas.close()
iras.close()
