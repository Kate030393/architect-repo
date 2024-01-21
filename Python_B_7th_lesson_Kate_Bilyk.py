# # TASK 1
# def mult_list(user_list: list):
#     result = 1
#     for el in user_list:
#         result *= el
#     return result
#
#
# new_list = [5, 6, 2]
# print(f"Result of multiplying all elements in list: {mult_list(new_list)}")


# # TASK 2
#
# def find_min(user_list: list):
#     return min(user_list)
#
#
# new_list = [5, 6, 2]
# print(f"The minimal element in list is {find_min(new_list)}")


# # TASK 3
#
# def find_primes(user_list: list):
#     result = 0
#     for i in user_list:
#         if i < 2:
#             continue
#         else:
#             j = 2
#             while j <= i//2:
#                 if i % j == 0:
#                     break
#                 j += 1
#             else:
#                 result += 1
#     return result
#
#
# new_list = [5, 6, 2, 3, 7, 10, 11, 97, 100]
# print(f"There are {find_primes(new_list)} prime numbers in the list")


# # TASK 4
#
# def count_deleted_el(user_list: list, element: int):
#     result = 0
#     while element in user_list:
#         user_list.remove(element)
#         result += 1
#     return result
#
#
# try:
#     user_list = [int(el) for el in input("Enter a list of numbers: ").split()]
#     element = int(input("Enter a number that you want to remove from the list: "))
#     print(f"Original list: {user_list}")
#     print(f"There are {count_deleted_el(user_list, element)} deleted numbers from the list")
#     print(f"Updated list: {user_list}")
# except ValueError as error:
#     print("Error of input. You entered not an integer")
# except Exception as error:
#     print(f"Error of input: {error}")


# # TASK 5
#
# def get_common_elements(list_1: list, list_2: list) -> list:
#     set_1 = set(list_1)
#     set_2 = set(list_2)
#     set_common_el = set_1.intersection(set_2)
#     list_common_el = list(set_common_el)
#     return list_common_el
#
#
# def extend_list(list_1: list, list_2: list) -> list:
#     list_1.extend(list_2)
#     return list_1
#
#
# first_list = [5, 0, 0, 0, 6, 2, 3, 7, 11, 97, 100, 0]
# second_list = [4, 0, 0, 6, 2, 3, 7, 10]
#
# print(f"The list of common elements: {get_common_elements(first_list, second_list)}")
# print(f"Union of two lists: {extend_list(first_list, second_list)}")

# # TASK 6
#
# def exponentiation(user_list: list, power: int):
#     updated_list = []
#     for el in user_list:
#         el **= power
#         updated_list.append(el)
#     return updated_list
#
# try:
#     # test_list = [4, 0, 0, 6, 2, 3, 7, 10]
#     test_user_list = [int(el) for el in input("Enter a list of numbers: ").split()]
#     degree = int(input("To what power to raise the elements: "))
#     print(f"Elements from your list in power {degree}: {exponentiation(test_user_list, degree)}")
# except ValueError as error:
#     print("Error of input. You entered not an integer")
# except Exception as error:
#     print(f"Error of input: {error}")
