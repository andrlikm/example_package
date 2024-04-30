from .internal_counts import add_one


def sum_all(numbers: list[int]) -> int:
    number_sum = 0
    for n in numbers:
        number_sum += n
    return number_sum


def add_two(n: int) -> int:
    n = add_one(n)
    n = add_one(n)
    return n

def count_average(nums):
    sum = 0.0
    for i in nums:
        sum += i
    return sum / len(nums)