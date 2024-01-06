def contains_word(input_str, word):
    return word in input_str


test_string = "Hello, World!"
search_word = "World"

if contains_word(test_string, search_word):
    print(f"'{test_string}' contains the word '{search_word}'.")
else:
    print(f"'{test_string}' does not contain the word '{search_word}'.")
