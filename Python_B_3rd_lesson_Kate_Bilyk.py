# TASK 1
try:
    user_choice = int(input("Which day of the week you want to see? Enter a number from 1 to 7: "))
    if user_choice < 1 or user_choice > 7:
        raise Exception("Error of input. Please enter a number from 1 to 7!")
    match user_choice:
        case 1:
            print("Monday is the 1st day of the week")
        case 2:
            print("Tuesday is the 2nd day of the week")
        case 3:
            print("Wednesday is the 3rd day of the week")
        case 4:
            print("Thursday is the 4th day of the week")
        case 5:
            print("Friday is the 5th day of the week")
        case 6:
            print("Saturday is the 6th day of the week")
        case 7:
            print("Sunday is the 7th day of the week")
except ValueError as error:
    print("Your input is not an integer. Please enter a number from 1 to 7!")
except Exception as error:
    print(f"{error}")

