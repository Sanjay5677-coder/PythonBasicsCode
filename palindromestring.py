def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]


test_string = "A man, a plan, a canal, Panama!"

if is_palindrome(test_string):
    print(f"{test_string} is a palindrome.")
else:
    print(f"{test_string} is not a palindrome.")
