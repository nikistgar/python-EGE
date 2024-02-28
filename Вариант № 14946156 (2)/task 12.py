a = "1" + "8" * 80
print(a)

while('18' in a or '288' in a or '3888' in a):
    if('18' in a):
        a = a.replace("18", "2")
    elif('288' in a):
        a = a.replace("288", "3")
    else:
        a = a.replace("3888","1")
print(a)