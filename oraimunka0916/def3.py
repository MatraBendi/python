a=1
def name():
	global a 
	a = 2 
	print(a)
a=3
name()

print(a)
