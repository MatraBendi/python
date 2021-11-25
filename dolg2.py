bekert = input("Add meg a fajl nevet: ")
try:
        olvasas = open((bekert), 'r')
        iras = open((bekert + "-out.txt"), 'wt')
except:
        print("Hibas a megadott fajl")
        exit()
line = olvasas.readline()
szamolo = 0
while line:
        szoveg = ""
        if szamolo % 2 != 0:
                szoveg += line.lower()
        else:
                szoveg += line.upper()
        szamolo += 1
        print(szamolo)
        iras.write(szoveg)
        print(szoveg, end="")
        line = olvasas.readline()
olvasas.close()
iras.close()
