import hashlib, bcrypt

jelszo = input("Kerem adjon megy egy jelszot: ")

sha = hashlib.sha512(jelszo.encode('utf-8')).hexdigest()

so = bcrypt.gensalt()

bcr = bcrypt.hashpw(jelszo.encode('utf-8'), so)

print(sha)
print()
print(bcr)
