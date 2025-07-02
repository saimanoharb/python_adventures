from basics.list_comprehension import ListComprehension
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""main.py"""
def main():
    """Main function to demonstrate list comprehension."""
    numbers = [1, 2, 3, 4, 5]
    logger.info(f"Original numbers: {numbers}")
    logger.info(f"Squared numbers: {ListComprehension.square_numbers(numbers)}")
    logger.info(f"Even numbers: {ListComprehension.filter_even_numbers(numbers)}")

if __name__ == "__main__":
    main() 
# This code is the entry point for the list comprehension demonstration.
# It imports the ListComprehension class and uses its methods to show how list comprehensions