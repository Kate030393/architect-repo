# TASK 2 Variant 1
try:
    number_1 = int(input("Enter 1st number: "))
    number_2 = int(input("Enter 2nd number: "))
    if number_1 < number_2:
        print(f"Your numbers in ascending order: {number_1}, {number_2}")
    elif number_1 > number_2:
        print(f"Your numbers in ascending order: {number_2}, {number_1}")
    else:
        print(f"You entered two identical numbers: {number_1} and {number_2}")
except ValueError as error:
    print("Your input is not an integer. Please enter only numbers!")
except Exception as error:
    print(f"Error: {error}")

# TASK 2 Variant 2
try:
    min_number = int(input("Enter 1st number: "))
    max_number = int(input("Enter 2nd number: "))
    if min_number < max_number:
        pass
    elif min_number > max_number:
        min_number, max_number = max_number, min_number
    else:
        print(f"You entered two identical numbers: {min_number} and {max_number}")
    print(f"Your numbers in ascending order: {min_number}, {max_number}")
except ValueError as error:
    print("Your input is not an integer. Please enter only numbers!")
except Exception as error:
    print(f"Error: {error}")


