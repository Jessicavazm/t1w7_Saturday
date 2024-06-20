from text_processing import count_words, unique_words, count_character, count_unique_characters, reverse_string

# You can rename variable's name to make it shorter and easier, that changes only occurs in the working file. 
# E.g" 
# import text_processing as tp
# from tp import count_words as cw


# Test string 
test_string = "Hello world hello"

# Using word_count module
print("Word count is", count_words(test_string))
print("Unique words:", unique_words(test_string))

# Using character_count module
print("Character count:",count_character(test_string))
print("Unique character count:",count_unique_characters(test_string))

# Using reverse module
print("Reverse string:",reverse_string(test_string))