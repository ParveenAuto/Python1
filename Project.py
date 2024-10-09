# Develop calculator
def calculator(n1, n2):
    operator=input("Which operator you want to run?\n +\n -\n *\n /\n ")
    n1=float(input("enter the first number"))
    n2=float(input("enter the second number"))
    
    if operator == '+':
        result = n1 + n2

    elif operator == '-':
        result = n1 - n2

    elif operator == '*':
        result = n1 * n2
   
    elif operator == '/':
        if n2 == 0:
            return "Error! Division by zero."
        result = n1/n2
    else:
            return "Invalid Operator!"
    return f"Result is: "

print(f"Your output is {calculator(n1, n2)}")

