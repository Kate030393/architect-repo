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


# TASK 3

def sum_in_range(first_num, second_num):
    if second_num == first_num:
        return first_num

    return second_num + sum_in_range(first_num, second_num - 1)

print(f"Result: {sum_in_range(2, 5)}")

# sum_in_range(2, 5) -> 5 + sum_in_range(2, 4) => 14
# sum_in_range(2, 4) -> 4 + sum_in_range(2, 3) => 9
# sum_in_range(2, 3) -> 3 + sum_in_range(2, 2) => 5
# sum_in_range(2, 2) => 2
# 2 + 3 + 4 + 5