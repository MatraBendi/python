cucc = input("Adj meg egy fajlnevet! ")
try:
        f = open(cucc,"wt")
        sor = input("Irj valamit! ")
        while sor:
                f.write(sor.lower())
                f.write("\n")
                sor = input("Irj meg valamit! ")
        f.close()
except:
        print("hiba a fajlkezelesben")
