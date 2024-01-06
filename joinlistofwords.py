def join_words(word_list):
    return ' '.join(word_list)


words_list = ["Hello,", "world!", "Hello,", "Python!", "Hello,", "World!"]

joined_string = join_words(words_list)

print(f"The list of words: {words_list}")
print(f"The joined string: {joined_string}")
