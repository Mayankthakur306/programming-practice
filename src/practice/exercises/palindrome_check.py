def is_palindrome(text: str) -> bool:
    clean_text = text.lower()
    return clean_text == clean_text[::-1]

# Examples
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False