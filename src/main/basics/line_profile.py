@profile
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

if __name__ == "__main__":
    example_function()
