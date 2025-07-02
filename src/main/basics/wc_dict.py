"""
This module provides functionality to count the number of words in a given string.
Functions:
    word_count(input_string: str): Returns the number of words in the provided input string.
"""
def word_count(input_string: str):
    """
    Counts the number of words in the input string.
    
    Args:
        input_string (str): The string to count words in.
        
    Returns:
        int: The number of words in the input string.
    """
    words = input_string.strip().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

if __name__ == "__main__":
    sample_text = "Hello world! This is a test. Hello again."
    counts = word_count(sample_text)
    print("Word counts:", counts)
    # Example output: Word counts: {'Hello': 2, 'world!': 1, 'This': 1, 'is': 1, 'a': 1, 'test.': 1, 'again.': 1}
    
