szoveg = input("Adjon meg szoveget: ")

try:
	x = int(input("Kerem irjon be szamokat: "))
	assert x>= 1 and x<=25
except ValueError:
	print("Nem szamot adatl meg")
	exit()
except:
	print("A szam 1 es 25kozott lehet")
	exit()

for i in szoveg:
	if(ord(i)+x> 122):
		print(ord(i)+x-25, end="" + " ")
	elif(ord(i)+x >=65 and ord(i)+x <=90):
		print(ord(i)+x ,end="" + " ")
	else:
		print(ord(i)+x , end="" + " ")
print("\n")
