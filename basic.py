print("Hello")

# array_append()


numbers = [1,2,3]
numbers.append(4)
print(numbers)

# add element at a specific position

numbers.insert(1,10)
print(numbers)

# add multiple elements

numbers.extend([5,6])
print(numbers)

# Remove elements from an array

numbers.remove(10)
print(numbers)

# Remove by index

numbers.pop(2)
print(numbers)

# Remove last element

numbers.pop()
print(numbers)

# Remove all elements

numbers.clear()
print(numbers)


# loop through an array

numbers = [1,2,3,4]
for num in numbers:
    print(numbers)

# loop with index

for i in range(len(numbers)):
    print(i , numbers[i])


# using enumerate

for index , value in enumerate (numbers):
    print(index , value)


# check if an element exists

if 4 in numbers :
    print("4 is in the list")

# length of the array

print(len(numbers))    


# sort of an array

numbers.sort()
print(numbers)

# reverse

numbers.sort(reverse = True)
print(numbers)

#example

arr = []

arr.append(5)
arr.append(10)
arr.append(15)

for num in arr:
    print(num)

# find the largest number

numbers = [4,2,9,1]
print(max(numbers))    


# print only the even numbers

numbers=[1,2,3,4,5,6,7]
for num in numbers:
    if num % 2 == 0:
        print(num)


 # Using slicing
 # reversed list.

numbers = [1,2,3,4]
reversed_numbers = numbers[::-1] 
print(reversed_numbers) 

# to convert back to a list

rev = list(reversed(numbers))

# Reverse using a loop

numbers = [1,2,3,4,5]
rev = []

for num in numbers:
    rev.insert(0,num)
    

    print(rev)  


# reverse a string array

names = ["Alice" , "Bob" , "Charlie"]
names.reverse()
print(names)

# reverse characters of a string using for loop

arr = ["python"]
s = arr[0]

for i in range(len(s)-1,-1,-1):
    print(s[i] , end = "")
