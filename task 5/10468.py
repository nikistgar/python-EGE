for x in range(1, 1001):
    j = bin(x)
    k = j[2::]
    p = k
    l = 0
    s = int(k)
    while (s > 0):
        l += s%10
        s //= 10
    k += str(l%2)
    d = int(k)
    l = 0
    while (d > 0):
        l += s%10
        d //= 10
    k += str(l%2)
    b = int(k, 2)
    if b > 77:
        break
print(x)