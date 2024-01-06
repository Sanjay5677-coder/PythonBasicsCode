def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_str if char in vowels)
    return vowel_count


test_string = "Hello, World!"

vowel_count = count_vowels(test_string)

print(f"The number of vowels in '{test_string}' is: {vowel_count}")
