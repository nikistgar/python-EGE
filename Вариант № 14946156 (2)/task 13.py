a = (bin(248)[2::])
b = (bin(255)[2::])
c = a[5::] + b
c = c.replace("0","1")
print(c)
print(int(c, 2)-1#255.255.255.255 не юзается
      )