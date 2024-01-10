# # TASK 1
#
# try:
#     decision = 1
#     while decision == 1:
#         text = input("Please print anything: ")
#         letters = 0
#         digits = 0
#         something = 0
#         for i in text:
#             if i.isalpha():
#                 letters += 1
#             elif i.isdigit():
#                 digits += 1
#             else:
#                 something += 1
#         print(f"You entered {letters} letters, {digits} digits and {something} other symbols")
#         decision = int(input("To continue input 1. To stop input 2: "))
#         if decision != 1 and decision != 2:
#             raise Exception("Please enter only 1 or 2!")
#         elif decision == 2:
#             print("Thank you! Goodbye!")
# except ValueError as error:
#     print("Error: your input is not an integer")
# except Exception as error:
#     print(f"Error: {error}")


# # TASK 2
#
# try:
#     decision = 1
#     while decision == 1:
#         text = input("Please print any text: ")
#         symbol = input("Please print a symbol for searching: ")
#         quantity = 0
#         for i in text:
#             if i == symbol:
#                 quantity += 1
#         print(f"Symbol \"{symbol}\" appears {quantity} times in your text")
#         decision = int(input("To repeat input 1. To stop input 2: "))
#         if decision != 1 and decision != 2:
#             raise Exception("Please enter only 1 or 2!")
#         elif decision == 2:
#             print("Thank you! Goodbye!")
# except ValueError as error:
#     print("Error: your input is not an integer")
# except Exception as error:
#     print(f"Error: {error}")


# # TASK 3
# try:
#     decision = 1
#     while decision == 1:
#         text = input("Please print any text: ")
#         old_word = input("Please enter a word that you want to change: ")
#         new_word = 0
#         if old_word not in text:
#             print("There is no such word in your text:(((")
#             decision = int(input("To repeat input 1. To stop input 2: "))
#         else:
#             new_word = input("Please enter a new word: ")
#             print(text.replace(old_word, new_word))
#             decision = int(input("To repeat input 1. To stop input 2: "))
#             if decision not in [1, 2]:
#                 raise Exception("Please enter only 1 or 2!")
#             elif decision == 2:
#                 print("Thank you! Goodbye!")
# except ValueError as error:
#     print("Error: your input is not an integer")
# except Exception as error:
#     print(f"Error: {error}")


# # TASK 4
#
# test_string = "Supercalifragilisticexpialidocious"
# print(f"1. The 3rd symbol is \"{test_string[2]}\"")
# print(f"2. The penultimate symbol is \"{test_string[-2]}\"")
# print(f"3. First 5 symbols are \"{test_string[0:5]}\"")
# print(f"4. The string without 2 last symbols: {test_string[:-2]}")
# print(f"5. All symbols with even indices: {test_string[::2]}")
# print(f"6. All symbols with odd indices: {test_string[1::2]}")
# print(f"7. All symbols in reverse order: {test_string[::-1]}")
# print(f"8. All symbols through one in reverse order: {test_string[::-2]}")
# print(f"9. The length of the string: {len(test_string)} symbols")


# # ADDITIONAL TASK 1
#
# text = """despite her advanced age, she was more of a nymphet than ever, with her apricot-colored  limbs,  in  her
# sub-teen tennis togs! winged gentlemen! no hereafter is acceptable if it does not produce her as she was then, in
# that Colorado  resort  between  Snow  and Elphinstone, with everything right: the white wide little-boy shorts,
# the slender waist, the  apricot  midriff,  the white  breast-kerchief  whose  ribbons went up and encircled her neck
# to end behind in a dangling knot leaving bare  her  gaspingly  young  and  adorable apricot  shoulder blades with that
# pubescence and those lovely gentle bones, and the smooth, downward-tapering back. her cap had a white peak. her racket
# had cost me a small fortune. idiot, triple idiot! i could have filmed her! i would have had her now with me, before my
# eyes, in the projection room of my pain and despair!"""
# digits = 0
# punctuation = 0
# exclamation_mark = 0
# new_text = ""
#
# i = 0
# while i < len(text):
#     if text[i].isdigit():
#         digits += 1
#     elif text[i] in [".", ",", ":", ";", " - "]:
#         punctuation += 1
#     elif text[i] == "!":
#         exclamation_mark += 1
#
#     if text[i] not in [".", "!", "?"]:
#         i += 1
#     else:
#         new_text += text[len(new_text):i]
#         new_text += text[i:i + 3].upper()
#         i += 3
# capitalized = new_text.capitalize()
# print(capitalized)
# print(f"In this text there are {digits} digits")
# print(f"In this text there are {punctuation} punctuation symbols")
# print(f"In this text there are {exclamation_mark} exclamation marks")


# ADDITIONAL TASK 2

length = 5
star = '* '
list = [range(1, length + 1)]
print(range(1, length + 1))
for i in range(1, length + 1):
    print(star * i)

# for i in list[::-1]:
#     print(star * i)
