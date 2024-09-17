def issubset(a1, a2):
    for x in a1:
        if x not in a2:
            return False
    return True

a1 = [1,3,4]
a2 = [4,5]


print(issubset(a1, a2))
