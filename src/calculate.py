from collections.abc import Iterable


def sum_even_number(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, retunr the sum of all even numbers in the iterable"""
    return sum(num for num in numbers if num % 2 == 0)
