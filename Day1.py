# function to calculate the square of a number

def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)

# Function to check if a number is even

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(is_even, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)


#function to multiply two numbers

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

product = reduce(multiply, numbers)

print("Numbers:", numbers)
print("Product of all numbers:", product)

