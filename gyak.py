str = input("Enter the String(Upper case):")
i = 0.
ch2 = ''
while str[i:]:
	ch = ord(str[i])
	if ch > 64 and ch < 91:
		ch2 += chr(ch+32)
	else:
		ch2 += chr(ch)
	i += 1
print(ch2)
