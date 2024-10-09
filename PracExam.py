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

# def life_in_weeks():
#     age = int(input("Enter your age:"))
#     years_left = 90 - age
#     weeks_left = years_left * 52 
    

#     print(f"You have {weeks_left} weeks left.")

# life_in_weeks()

#Que4 Love Count

# def calculate_love_score():
#     # Get both names as input
#     name1 = input("Enter the first person's name: ").lower()
#     name2 = input("Enter the second person's name: ").lower()
    
#     # Combine the names
#     combined_names = name1 + name2
    
#     # Count the occurrences of the letters in "TRUE"
#     true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
    
#     # Count the occurrences of the letters in "LOVE"
#     love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
    
#     # Combine the counts to form the love score (as a 2-digit number)
#     love_score = int(str(true_count) + str(love_count))
    
#     # Output the love score
#     print(f"Your love score is {love_score}.")

# # Call the function
# calculate_love_score()

#Que5 Write a program that returns True or False whether if a given year is a leap year.

# def is_leap_year(year):
#     if year%4 == 0:
#         return True
#     else:
#         return False
# year=int(input("enter the year"))

# print(is_leap_year(year))

    

