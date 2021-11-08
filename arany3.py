def fibs(n):
    f = []
    a = 0
    b = 1
    if n == 0 or n == 1:
        print n
    else:
        f.append(a)
        f.append(b)
        while len(f) != n:
            temp = a + b
            f.append(temp)
            a = b
            b = temp

    print f

fibs(10)
