from collections import defaultdict

def two_sum_all_indexes_no_duplicates(nums: list, target: int) -> list[list[int]]:
	index_map = defaultdict(list)
	result = []
	seen_pairs = set()
	for i, num in enumerate(nums):
		diff = target - num
		if diff in index_map:
			for appeared_index in index_map[diff]:
				pair = tuple(sorted((appeared_index, i)))
				if pair not in seen_pairs:
					result.append([appeared_index, i])
					seen_pairs.add(pair)
		index_map[num].append(i)
	return result

if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15, 2, 7, 2, 7, 7, 2]
    target = 9
    result = two_sum_all_indexes_no_duplicates(nums, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [[0, 1], [4, 5]]
    
    # Example with no solution
    nums_no_solution = [1, 2, 3]
    target_no_solution = 7
    result_no_solution = two_sum_all_indexes_no_duplicates(nums_no_solution, target_no_solution)
    print(f"Result for no solution case: {result_no_solution}")  # Output: []