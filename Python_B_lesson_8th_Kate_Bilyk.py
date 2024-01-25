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


# # TASK 3
#
# def sum_in_range(first_num, second_num):
#     if second_num < first_num:
#         second_num, first_num = first_num, second_num
#     elif second_num == first_num:
#         return first_num
#
#     return second_num + sum_in_range(first_num, second_num - 1)
#
#
# try:
#     user_number_1 = int(input("Enter first number: "))
#     user_number_2 = int(input("Enter second number: "))
#     print(f"The sum of all numbers between {user_number_1} and {user_number_2}: {sum_in_range(user_number_1, user_number_2)}")
# except ValueError:
#     print("Error of input. Please enter an integer!")
# except Exception as error:
#     print(f"Error: {error}")
#
# # # sum_in_range(2, 5) -> 5 + sum_in_range(2, 4) => 14
# # # sum_in_range(2, 4) -> 4 + sum_in_range(2, 3) => 9
# # # sum_in_range(2, 3) -> 3 + sum_in_range(2, 2) => 5
# # # sum_in_range(2, 2) => 2


# # TASK 4
#
# def find_min_sum_index(index: int, user_list: list, list_of_sums: list):
#     if index > len(user_list) - 10:
#         return list_of_sums.index(min(list_of_sums))
#
#     list_of_sums.append(sum(user_list[index: index + 10]))
#
#     return find_min_sum_index(index + 1, user_list, list_of_sums)
#
#
# import random
#
# my_test_list = [44, 6, 3, 22, 0, 98, 8, 3, 17, 7]
# list_100_numbers = []
#
# list_size = 100
# for i in range(list_size):
#     list_100_numbers.append(random.randint(1, 99))
#
# print(f"The start index of a list with minimal sum of 10 numbers: {find_min_sum_index(0, list_100_numbers, [])}")

