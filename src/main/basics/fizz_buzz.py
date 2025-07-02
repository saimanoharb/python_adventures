
def fizz_buzz(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        print(result or i)  # Print result if non-empty, otherwise print the number

if __name__ == "__main__":
    fizz_buzz(19)  # Example usage, prints FizzBuzz for numbers 1 to 100