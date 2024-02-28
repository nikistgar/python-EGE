for A in range(50,0,-1):
    for x in range (1,300):
        for y in range(1,300):
            if ((2*x + 3*y < 30) or (x + y >= A)):
                print(A)