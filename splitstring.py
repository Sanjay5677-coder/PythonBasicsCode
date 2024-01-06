def split_into_words(input_str):
    return input_str.split()


test_string = "Hello, world! Hello, Python! Hello, World!"

word_list = split_into_words(test_string)

print(f"The original string: {test_string}")
print(f"The list of words: {word_list}")
