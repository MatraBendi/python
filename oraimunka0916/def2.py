
def is_int(a):
	if type(a) == int:
		return True
	elif type(a) == float:
		return False

print(is_int(1)) 
print(is_int(1.)) 
print(is_int('1'))
