def sum(first,second):
    return first+second

def mulitply_with_sum(first, second):
    return (2*(sum(first,second)))

first = int(input("enter the first value : "))
second = int(input("enter the first value : "))
sum_value = sum(first, second)
print(f"Sum value is {sum_value}")

mul_value = mulitply_with_sum(first,second)
print(f"2 mulitplied : Sum value is {mul_value}")

mul_value2 = 3 * sum(first,second)
print(f"3 mulitplied : Sum value is {mul_value2}")


