def count_consonants(input_str):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = sum(1 for char in input_str if char in consonants)
    return consonant_count


test_string = "Hello, World!"

consonant_count = count_consonants(test_string)

print(f"The number of consonants in '{test_string}' is: {consonant_count}")
