import re

# # Home phone number checking
#
# home_phone_numbers = ["123456", "123", "+12345", "1234567"]
# home_number_str = "05789247568"
#
# def check_home_phone_number (*args):
#     for number in args:
#         if re.match(r"^\d{6}$", number):
#             print(f"Phone number {number} is correct")
#         else:
#             print(f"Phone number {number} is not correct")
#
#
# check_home_phone_number(*home_phone_numbers)
# check_home_phone_number(home_number_str)


# # Mobile phone number checking
#
# mob_phone_numbers = ["+380991234567", "380991234567", "+12345", "++1234567"]
# mob_number_str = "380991234567"
#
# def check_mob_phone_number (*args):
#     for number in args:
#         if re.match(r"^\+?\d{12}$", number):
#             print(f"Phone number {number} is correct")
#         else:
#             print(f"Phone number {number} is not correct")
#
#
# check_mob_phone_number(*mob_phone_numbers)
# check_mob_phone_number(mob_number_str)


# # Email checking
#
# emails_list = ["email_1@gmail.com", "email@gmail.com", "email3@gmail.com", "email_@gmail", "email_gmail.com", "email_@gmail.", "@gmail"]
# emails_str = "email-4@gmail.com"
#
# def check_email (*args):
#     for email in args:
#         if re.match(r"^[0-9a-zA-Z]+[._-]?[0-9a-zA-Z]+@[a-zA-Z0-9]+[.][a-zA-Z]{2,}$", email):
#             print(f"Email {email} is correct")
#         else:
#             print(f"Email {email} is not correct")
#
#
# check_email(*emails_list)
# check_email(emails_str)


# # Client`s full name checking
#
# user_names_list = ["User User User", "user user user", "user user", "user", "user7 user user", "user name user name", "a k e", "User_ User User"]
# user_name_str = "Билык Екатерина Викторовна"
#
# def check_name (*args):
#     for name in args:
#         if re.match(r"^[A-ZA-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZA-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZA-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}$", name):
#             print(f"User name '{name}' is correct")
#         else:
#             print(f"User name '{name}' is not correct")
#
#
# check_name(*user_names_list)
# check_name(user_name_str)


# # Password checking
#
# user_passwords_list = ["tgdhoi_TH1!", "8tgdhoi_TH1!", "t_T1!", "t", "1", "!!!!!!!", "gfdfygjnjooi", "YTGUGBKJHI", "tgdhoi_TH!", "tgdhoiTH5"]
# user_password_str = "tgdh_H1!"
#
# def check_password (*args):
#     for password in args:
#         if re.match(r"^.*(?=.{8})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$", password):
#             print(f"User password '{password}' is correct")
#         else:
#             print(f"User password '{password}' is not correct")
#
#
# check_password(*user_passwords_list)
# check_password(user_password_str)
