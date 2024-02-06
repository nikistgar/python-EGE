for x in range (1,1001):
    c = bin(x)
    c = c[2:]
    temp_1 = int(c)
    sum_1 = 0
    while temp_1 > 0:
        sum_1 += int(c)%10
        temp_1 //= 2
    c += str(sum_1%2)
    temp_2 = int(c)
    sum_2 = 0
    while temp_2 > 0:
        sum_2 += int(c) % 10
        temp_2 //= 2
    c += str(sum_2%2)
    n = int(c, 2)
    if n > 97:
        break
print (x)