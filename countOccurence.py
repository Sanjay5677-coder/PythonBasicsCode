def count_occurrences(input_str, target_word):
    return input_str.lower().count(target_word.lower())


test_string = "Hello, world! Hello, Python! Hello, World!"

word_to_count = "Hello"

occurrence_count = count_occurrences(test_string, word_to_count)

print(f"The word '{word_to_count}' occurs {occurrence_count} times in the string.")
