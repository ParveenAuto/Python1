#Que1 take a list with combination of 10 alaphabet and numbers and print all data one by one starting from 2nd no to second last number
#Solution
# mylist=("a", 3, 5, 6, 9, 90, "g", "r", "p", 7)
# for i in range(1, len(mylist)-1):
#     print(mylist[i])

#Que2 Given two arrays arr1[] and arr2[], the task is to find the number of elements in the union between these two arrays.
#Solution
# arr1=set([1,3,87,98,76])
# arr2=set([67,45,98,87,901,1,0])

# union = arr1.union(arr2)
# intersection=arr1.intersection(arr2)

# print(union)
# print(intersection)

#Que3 Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. 
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
#Solution

# def findelement(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
# arr=[1, 8, 9, 10]
# x=int(input("enter the number"))

# y= findelement(arr, x)
# print(y)


#Que4 Find largest element in the array

# def findlargestelement(arr):
#     if len(arr)==0:
#         return "Array is empty"
#     largest_element= max(arr)
#     return largest_element
# arr=[1,5,80,0,2345,12]
# print(f"Largest number in array is {findlargestelement(arr)}")

#Que5 Reverse array
# def reverse_array(input_arr):
#     reversed_array= input_arr[::-1]
#     return reversed_array
    
# input_arr= [1,9,6,0,4]
# print(reverse_array(input_arr))

#Que6 Given an array arr of positive integers. Reverse every sub-array group of size k.
# def reverse_in_groups(arr, n, k):
#     # Traverse the array in chunks of size k
#     for i in range(0, n, k):
#         # Reverse the sub-array from index i to i+k-1
#         arr[i:i+k] = arr[i:i+k][::-1]
#     return arr

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = len(arr)
# k = int(input("enter the value"))

# result = reverse_in_groups(arr, n, k)
# print(f"The array after reversing sub-arrays of size {k}: {result}")

#Que7 Find missing number in array

# def find_missing_array(arr):
#     n= len(arr)+1
#     total_sum= (n*(n+1))/2
#     array_sum = sum(arr)
#     missing_number= total_sum - array_sum
#     return missing_number
                
# arr= [1,2,3,4,5,6,8,9,10]
# print(f"Mising array is {find_missing_array(arr)}")

#Que7 Find all the numbers missing in array

def find_missing_numbers(arr, n):
    # Create a set of all numbers from 1 to n
    full_set = set(range(1, n + 1))
    
    # Convert the array to a set to remove duplicates and allow fast lookups
    arr_set = set(arr)
    
    # The missing numbers are the difference between the full set and the array set
    missing_numbers = list(full_set - arr_set)
    return missing_numbers

arr = [1, 2, 4, 6, 7, 9]
n = 9  
print(f"The missing numbers are: {find_missing_numbers(arr, n)}")
        




        



    








