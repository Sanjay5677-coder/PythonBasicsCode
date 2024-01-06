def remove_whitespaces_replace(input_str):
    return input_str.replace(" ", "")


original_string = "Hello, World!"

no_whitespace_string = remove_whitespaces_replace(original_string)

print(f"Original String: {original_string}")
print(f"String without Whitespaces: {no_whitespace_string}")
