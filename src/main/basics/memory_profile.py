from memory_profiler import profile

@profile
def memory_intensive_function():
    lst = [i for i in range(1000000)]
    return list(lst)

if __name__ == "__main__":
    memory_intensive_function()
