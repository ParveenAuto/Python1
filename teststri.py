#QueReverse string

def reverse_string_loop(input_str):
    reversed_str=""
    for char in input_str[::-1]:
        reversed_str += char
    return reversed_str
input_str=str(input("enter the value"))
reverse1=reverse_string_loop(input_str)
print(reverse1)

