import random

# # TASK 1
#
# random_list_size = 10
# random_list = []
# # my_list = [-5, -10, 7, -8, -3, -1, -9, -1, -4, -10]
#
# for i in range(random_list_size):
#     random_list.append(random.randint(-10, 10))
#
# sum_of_negative = 0
# sum_of_even = 0
# sum_of_odd = 0
# mult_index_3 = 1
# mult_between_min_max = 1
# sum_between_positive = 0
# min_index = random_list.index(min(random_list))
# max_index = random_list.index(max(random_list))
# first_positive = 0
# last_positive = 0
#
# for i in range(len(random_list)):
#     if random_list[i] > 0:
#         first_positive = i
#         break
# for i in range(len(random_list)):
#     if random_list[-abs(i)] > 0:
#         last_positive = -abs(i)
#         break
#
# sum_between_positive = sum(random_list[first_positive + 1:last_positive])
#
#
# if min_index > max_index:
#     max_index, min_index = min_index, max_index
# new_sliced_list = random_list[min_index + 1: max_index]
# for i in new_sliced_list:
#     mult_between_min_max *= i
#
#
# for i in range(len(random_list)):
#     if random_list[i] < 0:
#         sum_of_negative += random_list[i]
#
#     if random_list[i] % 2 == 0:
#         sum_of_even += random_list[i]
#
#     if random_list[i] % 2 != 0:
#         sum_of_odd += random_list[i]
#
#     if i % 3 == 0:
#         mult_index_3 *= random_list[i]
#
# print(random_list)
# print(f"The sum of all negative elements: {sum_of_negative}")
# print(f"The sum of all even elements: {sum_of_even}")
# print(f"The sum of all odd elements: {sum_of_odd}")
# print(f"The product of elements with multiple indices 3: {mult_index_3}")
# print(f"The multiply of elements between the minimum and maximum element: {mult_between_min_max}")
# print(f"The sum of elements between the first and the last positive elements: {sum_between_positive}")


# #  TASK 2
#
# random_list_size = 10
# random_list = []
# # my_list = [-5, -10, 7, -8, -3, -1, -9, -1, -4, -10]
# list_of_even = []
# list_of_odd = []
# list_of_negative = []
# list_of_positive = []
#
# for i in range(random_list_size):
#     random_list.append(random.randint(-10, 10))
#
# for i in random_list:
#     if i % 2 == 0 and i != 0:
#         list_of_even.append(i)
#
#     if i % 2 != 0 and i != 0:
#         list_of_odd.append(i)
#
#     if i < 0:
#         list_of_negative.append(i)
#
#     if i > 0:
#         list_of_positive.append(i)
#
# print(random_list)
# print(f"List with all even elemets: {list_of_even}")
# print(f"List with all odd elemets: {list_of_odd}")
# print(f"List with all negative elemets: {list_of_negative}")
# print(f"List with all positive elemets: {list_of_positive}")


# ADDITIONAL TASK

sum_main_diag = 0
side_diagonal = []
matrix = []

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99))

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

for i in range(len(matrix)):
    sum_main_diag += matrix[i][i]
print(f"The sum of main diagonal elements: {sum_main_diag}")

for i in range(len(matrix)):
    side_diagonal.append(matrix[i][9-i])
# print(side_diagonal)
print(f"The minimal element of side diagonal: {min(side_diagonal)}")
print(f"The maximal element of side diagonal: {max(side_diagonal)}")

try:
    column_choice = int(input("Please enter which column you want to print (from 1 to 10): "))
    if column_choice < 1 or column_choice > 10:
        raise Exception("Please enter a number from 1 to 10")
    column_list = []
    for i in range(len(matrix)):
        column_list.append(matrix[i][column_choice - 1])
    print(f"The column {column_choice}: {column_list}")

    raw_choice = int(input("Please enter which raw you want to print (from 1 to 10): "))
    if raw_choice < 1 or raw_choice > 10:
        raise Exception("Please enter a number from 1 to 10")
    print(f"The raw {raw_choice}: {matrix[raw_choice - 1]}")
except ValueError as error:
    print("Your input is not an integer. Please enter a number from 1 to 10")
except Exception as error:
    print(f"Error of input: {error}")

first_column = int(input("Enter the number for first column, that you want to replace: "))
second_column = int(input("Enter the number for second column, that you want to replace: "))

i = 0
for i in range(len(matrix)):
    while i < len(matrix):
        matrix[i][first_column - 1], matrix[i][second_column - 1] = matrix[i][second_column - 1], matrix[i][first_column - 1]
        i += 1
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()
