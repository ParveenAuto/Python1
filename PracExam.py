#Write a program to find the sum of the given series 1+2+3+ . . . . . . (n terms) 

# def mysum(n):
#     return n*(n+1)/2
# n=int(input("enter value"))
# sum_value=mysum(n)

# print (sum_value)

#Que 2. Extending a list
# cast=["a", "b"]
# cast.extend(["c", "d"])

# print(cast)

#Que 3. Life weekd left.

def life_in_weeks():
    age = int(input("Enter your age:"))
    years_left = 90 - age
    weeks_left = years_left * 52 
    

    print(f"You have {weeks_left} weeks left.")

life_in_weeks()
