#Que1: If set 1 contains set2
# def issubset(a1, a2):
#     for x in a1:
#         if x not in a2:
#             return False
#     return True

# a1 = [1,3,4]
# a2 = [4,5]
# print(issubset(a1, a2))

#Que2: If two sets are equal
# def equalsets(a1,a2):
#     a1.sort()
#     a2.sort()
#     if len(a1) != len(a2):
#         return False
#     for i in range(len(a1)):
#         if a1[i] != a2[i]:
#             return False
#     return True
    
# a1 = [1,4,5,2]
# a2 = [1,5,4,2]
# print(equalsets(a1,a2))