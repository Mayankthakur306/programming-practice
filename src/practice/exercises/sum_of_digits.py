def sum_of_digits_math(num: int) -> int:
    total = 0
    while num > 0:
        total += num % 10   # Grab the last digit
        num //= 10          # Truncate the last digit
    return total

# Example
print(sum_of_digits_math(1234))  # Output: 10