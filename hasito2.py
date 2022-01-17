import hashlib, bcrypt

jel = input("Kerek egy jelszot: ")

sha = hashlib.sha512(jel.encode('utf-8')).hexdigest()
so = bcrypt.gensalt()
bcr = bcrypt.hashpw(jel.encode('utf-8'),so)
print("sha512: ", sha)
print("bcrypt: ", bcr)
v = bcrypt.checkpw(jel.encode('utf-8'), bcr)
if v:
        print("Igen, egyezik a jelszo")
else:
        print("Nem egyezik")
