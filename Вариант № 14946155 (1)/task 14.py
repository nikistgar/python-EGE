# Сколько единиц содержится в двоичной записи значения выражения: 42020 + 22017 – 15?

c = 4**2020 + 2**2017 - 15

s = ""
def perevod(c, s):
    while (c > 0):
        s += str((c % 2))
        c = c // 2
        print(c)
    k = s[::-1]
    return k

f = perevod(c, s)

x = f.count("1")
print(x)