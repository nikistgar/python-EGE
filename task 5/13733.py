for x in range (1, 1001):
    s = bin(x)
    y = s[2:]
    temp_1 = int(y)
    sum_1 = 0
    while temp_1 > 0:
        sum_1 += temp_1%10
        temp_1 //= 10
    y += str(sum_1%2)
    temp_2 = int(y)
    sum_2 = 0
    while temp_2 > 0:
        sum_2 += temp_2 % 10
        temp_2 //= 10
    y += str(sum_2%2)
    r = int(y, 2)
    if r > 83:
        break
print(r)