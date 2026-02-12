def is_palindrome(text):
    """Check if a string is a palindrome, ignoring spaces and case."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test the function
if __name__ == "__main__":
    test_strings = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "level"
    ]
    
    for string in test_strings:
        result = is_palindrome(string)
        print(f"'{string}' is a palindrome: {result}")