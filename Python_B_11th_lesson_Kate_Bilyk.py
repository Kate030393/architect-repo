ORIGINAL_FILE = "original_text.txt"
NEW_FILE = "get_7_letters_words.txt"

# TASK 1

with open(ORIGINAL_FILE, "r") as file:
    orig_text = file.read()
    char_remove = [',', '.', '"', '!', '?', ':', '(', ')']
    for char in char_remove:
        orig_text = orig_text.replace(char, '')
    orig_text = orig_text.split()
    print(orig_text)
    long_wrds = " ".join([el for el in orig_text if len(el) >= 7])


with open(NEW_FILE, "w") as copied_file:
    copied_file.write(long_wrds)

with open(NEW_FILE, "r") as new_file:
    print(new_file.read())


# # TASK 2
#
# with open(ORIGINAL_FILE, "r") as file:
#     orig_text = file.read().split()
#     print(len(orig_text))


# # TASK 3
#
# with open(ORIGINAL_FILE, "r") as file:
#     orig_text = file.read()
#     print(f"Original text: {orig_text}")
#     unwished_word = input("Enter which word you want to replace: ").lower()
#     replace_element = "*" * len(unwished_word)
#     orig_text = orig_text.replace(unwished_word, replace_element).replace(unwished_word.capitalize(), replace_element)
#     print(f"Result: {orig_text}")
#     print(f"Statistic: {orig_text.count(replace_element)} replaces of word '{unwished_word}'")
