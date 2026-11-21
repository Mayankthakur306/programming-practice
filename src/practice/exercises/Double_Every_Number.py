def double_numbers(nums: list[int]) -> list[int]:
    doubled = []
    for num in nums:
        doubled.append(num * 2)
    return doubled

print(double_numbers([1, 4, 7, 10]))  # Output: [2, 8, 14, 20]