def issubset(a1, a2):
    for x in a1:
        if x not in a2:
            return False
    return True

a1 = [1,2,4,6]
a2 = [1,4]


print(issubset(a1, a2))

