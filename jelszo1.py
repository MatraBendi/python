import hashlib, bcrypt
jelszo = input("adjon meg egy jelszot! ")
sha = hashlib.sha512(jelszo.encode("utf-8")).hexdigest()
so = bcrypt.gensalt()
bcr = bcrypt.hashpw(jelszo.encode("utf8"),so)
jelszo2 = input("ugyanazt add meg: ")
jo = bcrypt.checkpw(jelszo2.encode("utf8"),bcr)

print (sha)
print (bcr)
if jo:
        print("ugyes vagy!")
else:
        print("bena vagy!") 
