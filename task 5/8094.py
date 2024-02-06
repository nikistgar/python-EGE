for x in range(1 , 1001):
    s = ""
    while x > 0:
        s += str(x % 2)
        x //= 2
    dvoich = s[::-1]
    c = int(dvoich)
    h = 0
    while c > 0:
        delim = c % 10
        if (delim >= 1):
            h += delim
        c //= 10
    h %= 2
    dvoich += str(h)
    y = int(dvoich)
    i = 0
    while y != 0:
        delim2 = y % 10
        if (delim2 >= 1):
            i += delim
        y //= 10
    i %= 2
    dvoich += str(i)
    k = int(dvoich, 2)
    if (k >= 43):
        break
print(k)