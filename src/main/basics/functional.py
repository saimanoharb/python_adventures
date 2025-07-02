# Using lambda to create an anonymous function
square = lambda x: x * x
print(square(5)) # Output: 25
# Using map to apply a function to a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16