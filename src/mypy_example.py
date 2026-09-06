from typing import List


def add_two(nums: List[int]):
    return [num + 2 for num in nums]


if __name__ == "__main__":
    add_two([1, 2.0, 3])
