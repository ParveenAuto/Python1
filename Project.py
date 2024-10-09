# Develop calculator
def add(n1, n2):
    if symbol == '+':
        return n1 + n2
#def subtract(n1, n2):
    elif symbol == '-':
        return n1 - n2
#def multiply(n1, n2):
    elif symbol == '*':
        return n1 * n2
#def divide(n1, n2):
    else:
        return n1/n2

symbol=input("Which operator you want to run? +, -, *, / ")
n1=int(input("enter the number"))
n2=int(input("enter the number"))


print(f"Your output is ")

