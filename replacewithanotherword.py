def replace_word(input_str, old_word, new_word):
    return input_str.replace(old_word, new_word)


original_string = "Hello, World! Hello, Python!"

old_word_to_replace = "Hello"
new_word = "Hi"

modified_string = replace_word(original_string, old_word_to_replace, new_word)

print(f"Original String: {original_string}")
print(f"Modified String: {modified_string}")
