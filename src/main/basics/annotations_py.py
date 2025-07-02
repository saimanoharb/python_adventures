age: int = 25  # This means age is an integer
name: str = "Alice"  # This means name is a string

age = "twenty-five"  # Tools like mypy will warn you: "age should be an int"
print(age)  # Output: twenty-five

# Reading input from the user
name = input("Enter your name: ")
s = "Hello," + name
print(s)

# with open("output.txt", "w") as file:
#     file.write(s + "\n")
#     file.write("This is a line of text.\n")
#     file.write("Another line.\n")

file_path = 'output.txt'

with open(file_path, 'r') as file:
    while True:
        line = file.readline()
        if not line:  # End of file
            break
        print(line.strip())


def add(a, b):
    """
    Add two numbers and return the result.
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

print(add.__doc__)