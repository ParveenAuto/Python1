def issubset(a1, a2):
    for x in a1:
        if x not in a2:
            return False
    return True

a1 = int(input("enter the value"))
a2 = int(input("enter the value"))


print(issubset(a1, a2))
