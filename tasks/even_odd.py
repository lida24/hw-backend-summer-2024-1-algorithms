__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    even_nums, odd_nums = [], []
    result = 0
    for elem in numbers:
        if elem % 2 == 0:
            even_nums.append(elem)
        else:
            odd_nums.append(elem)
    if len(even_nums) != 0 and len(odd_nums) != 0:
        result = sum(even_nums) / sum(odd_nums)
    return result
