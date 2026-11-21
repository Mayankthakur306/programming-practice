def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("List cannot be empty")
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest

print(find_max([12, 45, 7, 89, 23]))  # Output: 89