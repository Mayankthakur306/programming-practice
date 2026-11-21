def word_count(sentence: str) -> int:
    words = sentence.split()
    return len(words)

print(word_count("Python is fun to learn"))  # Output: 5