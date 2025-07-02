def move_zeros(nums: list[int]) -> None:
    """
    Moves all zeroes in the list to the end while maintaining the order of non-zero elements.
    Operates in-place.
    """
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

if __name__ == "__main__":
    # Example usage
    nums = [0, 1, 0, 3, 12]
    print(f"Original list: {nums}")
    move_zeros(nums)
    print(f"List after moving zeros: {nums}")
    
    # Example with all zeros
    nums_all_zeros = [0, 0, 0]
    print(f"Original list: {nums_all_zeros}")
    move_zeros(nums_all_zeros)
    print(f"List after moving zeros: {nums_all_zeros}")