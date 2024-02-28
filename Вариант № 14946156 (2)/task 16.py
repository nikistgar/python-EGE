def F(a):
    if a == 1:
        return 1
    if a == 2:
        return 3
    if a > 2:
        return F(a-1) * a + F(a-2) * (a-1)
print(F(5))