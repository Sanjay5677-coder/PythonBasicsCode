def find_last_occurrence(input_str, target_word):
    return input_str.lower().rfind(target_word.lower())


test_string = "Hello, world! Hello, Python! Hello, World!"

word_to_find = "Hello"

last_occurrence_index = find_last_occurrence(test_string, word_to_find)

if last_occurrence_index != -1:
    print(f"The last occurrence of the word '{word_to_find}' starts at index {last_occurrence_index}.")
else:
    print(f"The word '{word_to_find}' is not present in the string.")
