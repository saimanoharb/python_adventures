def two_sum_unique_value_pairs(nums, target):
    seen = set()
    result = set()
    
    for num in nums:
        diff = target - num
        pair = tuple(sorted((num, diff)))
        if diff in seen:
            result.add(pair)
        seen.add(num)
    
    return [list(pair) for pair in result]
if __name__ == "__main__":
    # Example usage
    squares_dict = {x: x * x for x in range(5)}
    print(squares_dict)
    sentence = "hello world"
    vowels = {char for char in sentence if char in "aeiou"}
    print(vowels) # Output: {'e', 'o'}
# Explanation: Collects unique vowels f
    nums = [2, 7, 11, 15, 2, 7]
    target = 9
    result = two_sum_unique_value_pairs(nums, target)
    print(f"Unique pairs of numbers that add up to {target}: {result}")  # Output: [[2, 7]]
    
    # Example with no solution
    nums_no_solution = [1, 2, 3]
    target_no_solution = 7
    result_no_solution = two_sum_unique_value_pairs(nums_no_solution, target_no_solution)
    print(f"Result for no solution case: {result_no_solution}")  # Output: []