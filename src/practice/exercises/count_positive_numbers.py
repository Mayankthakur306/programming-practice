def count_positives(nums: list[int]) -> int:
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count

print(count_positives([-5, 3, 0, 8, -2, 12]))  # Output: 3