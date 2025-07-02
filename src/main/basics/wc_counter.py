from collections import Counter

def word_count(input_string: str) -> dict:
    words = input_string.split()  # Split the string into words
    return dict(Counter(words))  # Use Counter to count occurrences and convert to a dictionary

if __name__ == "__main__":
    sample_text = "Hello world! This is a test. Hello again."
    counts = word_count(sample_text)
    print("Word counts:", counts)
    # Example output: Word counts: {'Hello': 2, 'world!': 1, 'This': 1, 'is': 1, 'a': 1, 'test.': 1, 'again.': 1}