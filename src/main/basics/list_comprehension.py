from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""
list_comprehension.py

Demonstrates the use of list comprehensions in Python.
"""

class ListComprehension:
    @staticmethod
    def square_numbers(numbers: List[int]) -> List[int]:
        """Returns a list of squares for the given list of numbers."""
        logger.info("Squaring numbers using list comprehension.")
        try:
            return [n ** 2 for n in numbers]
        except TypeError as e:
            logger.error(f"Input must be a list of integers. Error: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []

    @staticmethod
    def filter_even_numbers(numbers: List[int]) -> List[int]:
        """Returns a list containing only the even numbers from the input list."""
        logger.info("Filtering even numbers using list comprehension.")
        try:
            return [n for n in numbers if n % 2 == 0]
        except TypeError as e:
            logger.error(f"Input must be a list of integers. Error: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []

if __name__ == "__main__":

    # Example usage
    numbers = [1, 2, 3, 4, 5]
    logger.info(f"Original numbers: {numbers}")
    logger.info(f"Squared numbers: {ListComprehension.square_numbers(numbers)}")
    logger.info(f"Even numbers: {ListComprehension.filter_even_numbers(numbers)}")

    # Example with invalid input
    invalid_numbers = [1, 'a', 3]
    logger.info(f"Original numbers: {invalid_numbers}")
    logger.info(f"Squared numbers: {ListComprehension.square_numbers(invalid_numbers)}")
    logger.info(f"Even numbers: {ListComprehension.filter_even_numbers(invalid_numbers)}")