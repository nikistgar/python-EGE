
a = []
for x in range(100, 3001):
    k = bin(x)[3::]
    l = int(k)
    p = int(str(l), 2)
    c = x - p
    if c not in a:
        a.append(c)
print(len(a))