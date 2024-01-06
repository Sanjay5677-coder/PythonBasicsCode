def calculate_string_length(input_str):
    length = 0
    for char in input_str:
        length += 1
    return length


test_string = "Hello, World!"

string_length = calculate_string_length(test_string)

print(f"The length of '{test_string}' is: {string_length}")
