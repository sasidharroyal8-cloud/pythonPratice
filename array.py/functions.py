def add(a,b):
    return a+b 

res = add(2,4)
print(res)

# functions to print all elements of an array

def print_array(arr):
    for items in arr:
        print(items)

numbers = [1,2,3,4]
print_array(numbers)   


#Function to find sum of array elements

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = [5,10,15]
print(sum_array(numbers))

#Function to find the largest number in an array

def max_array(arr):
    return max(arr)

numbers = [4,9,2,7]
print(max_array(numbers))

#Function to count elements in an array

def count_array(arr):
    return len(arr)

numbers = [1,2,3,4,5]
print(count_array(numbers))

#Function to reverse an array

def reverse_array(arr):
    return arr[::-1]

numbers = [1,2,3,4,5]
print(reverse_array(numbers))

#Function to check if element exists in an array

def find_element(arr , target):
    if target in arr:
        return "Found"
    else:
        return "Not Found"
    
numbers = [5,6,7]
print(find_element(numbers , 6))

#Function to print only even numbers

def even_numbers(arr):
    for num in arr:
        if num % 2 == 0:
            print(num)

numbers = [1,2,3,4,5,6]
print(even_numbers(numbers))       


#Function to add an element to an array

def add_element(arr , value):
    arr.append(value)
    return arr

numbers = [1,2,3]
print(add_element(numbers,4))

# Example

def average(arr):
    return sum(arr) / len(arr)

numbers = [10,20,30]
print(average(numbers))

#Write a function that returns the second largest number in an array.

def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

print(second_largest([10,20,30,40]))

# Return values

def get_greeting():
    return "Hello from a message"

print(get_greeting())

# a function with one argument

