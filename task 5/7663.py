for x in range (100, 1000):
    y = str(x)[0]
    u = str(x)[1]
    i = str(x)[2]
    a = int(y) + int(u)
    b = int(u) + int(i)
    if (a > b):
        n = str(a) + str(b)
    elif (a < b):
        n = str(b) + str(a)
    if (int(n) == 1412):
        break
print(x)
