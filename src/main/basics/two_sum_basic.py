# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(nums: list[int], target: int) -> list[int]:
	seen_map = {}
	for i in range(len(nums)):
		diff = target - nums[i]
		if diff in seen_map:
			return [seen_map[diff], i]
		seen_map[nums[i]] = i
	return None  # Return None if no solution is found

if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [0, 1]
    
    # Example with no solution
    nums_no_solution = [1, 2, 3]
    target_no_solution = 7
    result_no_solution = two_sum(nums_no_solution, target_no_solution)
    print(f"Result for no solution case: {result_no_solution}")  # Output: None
