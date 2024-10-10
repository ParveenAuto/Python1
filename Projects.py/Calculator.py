# Develop Calculator
# def calculator(n1, n2):
#      if operator == '+':
#          return n1 + n2

#      elif operator == '-':
#          return n1 - n2

#      elif operator == '*':
#          return n1 * n2
   
#      else:
#          return n1/n2
 

# operator=input("Which operator you want to run?\n +\n -\n *\n /\n ")
# n1=float(input("enter the first number"))
# n2=float(input("enter the second number"))
# print(f"Your output is {calculator(n1, n2)}")



# Develop calculator1
# def calculator():
#     operator=input("Which operator you want to run?\n +\n -\n *\n /\n ")
#     n1=float(input("enter the first number"))
#     n2=float(input("enter the second number"))
    
#     if operator == '+':
#         result = n1 + n2

#     elif operator == '-':
#         result = n1 - n2

#     elif operator == '*':
#         result = n1 * n2
   
#     elif operator == '/':
#         if n2 == 0:
#             return "Error! Division by zero."
#         result = n1/n2
#     else:
#             return "Invalid Operator!"
#     return f"Result is: "

# print(f"Your output is {calculator()}")


#Develop Caclulator3
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
 
operations = { 
    "+": add, 
    "-": subtract,
    "*":multiply,
    "/":divide, 
}
def calculator():
    should_accumulate = True
    num1=float(input("What is the first number:"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol= input("Pick an operation:")
        num2=float(input("What is the second number:")) 
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Tupe 'y' to continue calculationg with {answer}, or tye 'n' to start a new calculation")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
            
calculator()