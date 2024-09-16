#function input 4 numbers in one go and print them , sum first two values and sum remianing 2 vlues
def input_numbers(input_1, input_2):
    return input_1+input_2
def input_numbers(input_3, input_4):
    return input_3+input_4


input_1=int(input("Enter the number"))
input_2=int(input("Enter the number"))
input_3=int(input("Enter the number"))
input_4=int(input("Enter the number"))

sum_value1=input_numbers(input_1, input_2)
print(f" Sum of first and second number is {sum_value1}")

sum_value2=input_numbers(input_3, input_4)
print(f" Sum of third and fourth number is {sum_value2}")

mul_value3=sum_value1*sum_value2
print(f"Multiplication of values is {mul_value3}")


