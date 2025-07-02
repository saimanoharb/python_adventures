import cProfile
# def example():
#     total = 0
#     for i in range(100000000000):
#         total += i
#     return total

# cProfile.run('example()')
def optimized_example():
    return sum(range(1000000))

cProfile.run('optimized_example()')
