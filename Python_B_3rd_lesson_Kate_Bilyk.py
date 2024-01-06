# # TASK 1
# try:
#     user_choice = int(input("Which day of the week you want to see? Enter a number from 1 to 7: "))
#     if user_choice < 1 or user_choice > 7:
#         raise Exception("Error of input. Please enter a number from 1 to 7!")
#     match user_choice:
#         case 1:
#             print("Monday is the 1st day of the week")
#         case 2:
#             print("Tuesday is the 2nd day of the week")
#         case 3:
#             print("Wednesday is the 3rd day of the week")
#         case 4:
#             print("Thursday is the 4th day of the week")
#         case 5:
#             print("Friday is the 5th day of the week")
#         case 6:
#             print("Saturday is the 6th day of the week")
#         case 7:
#             print("Sunday is the 7th day of the week")
# except ValueError as error:
#     print("Your input is not an integer. Please enter a number from 1 to 7!")
# except Exception as error:
#     print(f"{error}")
#
#
# # TASK 2 Variant 1
# try:
#     number_1 = int(input("Enter 1st number: "))
#     number_2 = int(input("Enter 2nd number: "))
#     if number_1 < number_2:
#         print(f"Your numbers in ascending order: {number_1}, {number_2}")
#     elif number_1 > number_2:
#         print(f"Your numbers in ascending order: {number_2}, {number_1}")
#     else:
#         print(f"You entered two identical numbers: {number_1} and {number_2}")
# except ValueError as error:
#     print("Your input is not an integer. Please enter only numbers!")
# except Exception as error:
#     print(f"Error: {error}")
#
# # TASK 2 Variant 2
# try:
#     min_number = int(input("Enter 1st number: "))
#     max_number = int(input("Enter 2nd number: "))
#     if min_number < max_number:
#         pass
#     elif min_number > max_number:
#         min_number, max_number = max_number, min_number
#     else:
#         print(f"You entered two identical numbers: {min_number} and {max_number}")
#     print(f"Your numbers in ascending order: {min_number}, {max_number}")
# except ValueError as error:
#     print("Your input is not an integer. Please enter only numbers!")
# except Exception as error:
#     print(f"Error: {error}")


# TASK 3
try:
    decision = 1
    while decision == 1:
        number_1 = int(input("Enter 1st number: "))
        action = input("Choose an action ( + or - or * or / ): ")
        if action not in "+-*/":
            raise Exception("Error of input. Please enter + or - or * or /")
        number_2 = int(input("Enter 2nd number: "))
        match action:
            case "+":
                print(f"Sum result: {number_1 + number_2}")
            case "-":
                print(f"Difference result: {number_1 - number_2}")
            case "*":
                print(f"Division result: {number_1 * number_2}")
            case "/":
                print(f"Multiplication result: {number_1 / number_2}")
        decision = int(input("To continue input 1. To stop input 2: "))
        if decision != 1 and decision != 2:
            raise Exception("Please enter only 1 or 2!")
        elif decision == 2:
            print("Thank you! Goodbye!")
except ValueError as error:
    print("Your input is not an integer")
except Exception as error:
    print(f"Error: {error}")


