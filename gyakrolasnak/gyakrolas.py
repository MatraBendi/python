#!/usr/bin/env python3

#madlips
nev = input("Irjon be egy nevet: ")
szin = input("Irjon be egy szint: ")
szam = int(input("Irjon be egy szamot: "))
varos = input("Adjon meg egy varost: ")
print("\n" + nev + " szerint a " + szin + " ronda szin")
if szam < 5:
	print(nev + " nem iszik sokat")
else:
	print(nev + " sokat iszik")
print(nev + " kedvenc varosa: " + varos + "\n")


#random nev generator
#1 nev
print("Egy random nevet ossze rakott: ")
import random
csaladnev = ["Nagy", "Kiss", "Huszar", "Szabo", "Varga", "Balogh", "Papp", "Takacs", "Olah"]
keresztnev = ["Pista", "Bence", "Adam", "Zsofi", "Hanga", "Fanni", "Gyula", "Lilla", "Tomi"]
group = [] 
egybenev = random.choice(csaladnev) +" " +  random.choice(keresztnev)
group.append(egybenev)
print(egybenev)

#nev generator sok nev
print("\nSok random nevet ossze rakott: ")
def nev():
	import random
	group2 = []
	egybenev2 = random.choice(csaladnev) + " " +  random.choice(keresztnev)
	print(egybenev2)

for group2 in range(3):
    nev()

#lotto szam generator
print("\nEheti lotto szamok: ")
def lotto():
	import random
	szamok = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	group3 = []
	vegso = random.choice(szamok)
	print(vegso, end=" ")
for group3 in range(3):
	lotto()

#talad ki a szamot
szamok = [1 , 2]
bekert = int(input("\n\nAdjon meg egy szamot(1 vagy 2): "))
vegso2 = random.choice(szamok)
if vegso2 == bekert:
	print("Eltalalta a samot")
else:
	print("Nem talalta el")


#listas parancsok----------

lista1 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
lista2 = lista1[:]
print("\nA listaban ezek az elemek talalhatok: 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 ")

#lista vegere hozza adni
bekert2 = int(input("\nA lista vegehez adjunk hozza egy szamot: "))
lista1.append(bekert2)
print(lista1)

#listaba beszuras
bekert3 = int(input("\nMondja meg melyik helyre szurjam be a szamot: "))
lista2.insert(bekert3, bekert2)
print(lista2)
