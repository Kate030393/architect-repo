# TASK 1

# def get_number_pow(number, number_pow):
#     if number_pow <= 1:
#         return number
#
#     return number * get_number_pow(number, number_pow - 1)
#
#
# print(get_number_pow(2, 3))

# get_number_pow(2, 3) -> 2 * get_number_pow(2, 2) => 8
# get_number_pow(2, 2) -> 2 * get_number_pow(2, 1) => 4
# get_number_pow(2, 1) => 2

# # TASK 2
#
# def draw_stars(number):
#     if number == 1:
#         return "*"
#     elif number < 1:
#         return "Error. Enter a number bigger than 0"
#     return "* " + draw_stars(number - 1)
#
#
# try:
#     user_number = int(input("What number of stars do you want to print: "))
#     print(f"Result: {draw_stars(user_number)}")
# except ValueError:
#     print("Error of input. Please enter an integer!")
# except Exception as error:
#     print(f"Error: {error}")
#
# # draw_stars(4) -> "*" + draw_stars(3) => "****"
# # draw_stars(3) -> "*" + draw_stars(2) => "***"
# # draw_stars(2) -> "*" + draw_stars(1) => "**"
# # draw_stars(1) -> "*"


# TASK 3

def sum_in_range(first_num, second_num):
    if second_num < first_num:
        second_num, first_num = first_num, second_num
    elif second_num == first_num:
        return first_num

    return second_num + sum_in_range(first_num, second_num - 1)


try:
    user_number_1 = int(input("Enter first number: "))
    user_number_2 = int(input("Enter second number: "))
    print(f"The sum of all numbers between {user_number_1} and {user_number_2}: {sum_in_range(user_number_1, user_number_2)}")
except ValueError:
    print("Error of input. Please enter an integer!")
except Exception as error:
    print(f"Error: {error}")

# # sum_in_range(2, 5) -> 5 + sum_in_range(2, 4) => 14
# # sum_in_range(2, 4) -> 4 + sum_in_range(2, 3) => 9
# # sum_in_range(2, 3) -> 3 + sum_in_range(2, 2) => 5
# # sum_in_range(2, 2) => 2
