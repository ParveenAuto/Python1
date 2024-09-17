def issubset(a1, a2):
    for x in a1:
        if x not in a2:
            return False
    return True

a1 = [11,7,1]
a2 = [11,3,7,1,7]


print(issubset(a1, a2))
