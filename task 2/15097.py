print("x y z")

for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x == z ) or (x <= (y and z))) == 0:
                print(x, y, z)

#yzx