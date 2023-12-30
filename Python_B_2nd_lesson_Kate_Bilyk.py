# Task 1

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
action = input("Enter one function from the list min/max/average: ")

# Variant 1
if action == "min":
    if num_2 >= num_1 <= num_3:
        print("Minimal number:", num_1)
    elif num_1 >= num_2 <= num_3:
        print("Minimal number:", num_2)
    else:
        print("Minimal number:", num_3)
elif action == "max":
    if num_2 <= num_1 >= num_3:
        print("Maximal number:", num_1)
    elif num_1 <= num_2 >= num_3:
        print("Maximal number:", num_2)
    else:
        print("Maximal number:", num_3)
elif action == "average":
    print("Average of numbers:", (num_1 + num_2 + num_3) / 3)
else:
    print("Error. Choose function from the list")

# Variant 2
list_of_numbers = [num_1, num_2, num_3]
if action == "max":
    max_n = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max_n:
            max_n = i
    print(max_n)
elif action == "min":
    min_n = list_of_numbers[0]
    for i in list_of_numbers:
        if i < min_n:
            min_n = i
    print(min_n)
elif action == "average":
    print("Average of numbers:", (num_1 + num_2 + num_3) / 3)
else:
    print("Error. Choose function from the list")

# Variant 3
functions = {
    'min': lambda a,b,c:  min(a,b,c),
    'max': lambda a,b,c:  max(a,b,c),
    'average': lambda a,b,c:  (a+b+c)/3
}

for key in functions:
    if key == action:
        print(functions[key](num_1, num_2, num_3))

# Task 2

meters = int(input("Enter the distance in meters: "))
convert_type = input("Choose the unit mile/inch/yard/: ")
convert_dict = {
    "mile": lambda x: x / 1609,
    "inch": lambda x: x / 0.0254,
    "yard": lambda x: x / 0.9144,
}
for key in convert_dict:
    if key == convert_type:
        print(convert_dict[key](meters))
    else:
        print("Error. Choose correct unit")

