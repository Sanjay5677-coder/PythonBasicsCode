def find_first_occurrence(input_str, target_word):
    return input_str.lower().find(target_word.lower())


test_string = "Hello, world! Hello, Python! Hello, World!"

word_to_find = "Hello"

first_occurrence_index = find_first_occurrence(test_string, word_to_find)

if first_occurrence_index != -1:
    print(f"The first occurrence of the word '{word_to_find}' starts at index {first_occurrence_index}.")
else:
    print(f"The word '{word_to_find}' is not present in the string.")
