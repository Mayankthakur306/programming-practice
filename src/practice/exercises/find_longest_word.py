def longest_word(words: list[str]) -> str:
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(["cat", "elephant", "dog", "giraffe"]))  # Output: elephant