from collections import defaultdict

def two_sum_all_indexes(nums: list, target: int) -> list[list[int]]:
	index_map = defaultdict(list)
	result = []
	
	for i, num in enumerate(nums):
		diff = target - num
		if diff in index_map:
			for appeared_index in index_map[diff]:
				result.append([appeared_index, i])
		index_map[num].append(i)
	return result

if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15, 2, 7]
    target = 9
    result = two_sum_all_indexes(nums, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [[0, 1], [4, 5]]
    
    # Example with no solution
    nums_no_solution = [1, 2, 3]
    target_no_solution = 7
    result_no_solution = two_sum_all_indexes(nums_no_solution, target_no_solution)
    print(f"Result for no solution case: {result_no_solution}")  # Output: []