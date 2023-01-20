
def password_validator(command):
    is_valid = True
    is_letter_and_digit = False
    if len(command) > 10 or len(command) < 6:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    count = 0
    for i in str(command):
        if ord(i) in range(48, 58):
            count += 1
        if ord(i) not in range(48, 58) and ord(i) not in range(65, 91) and ord(i) not in range(97, 123):
            is_letter_and_digit = True
            is_valid = False
    if is_letter_and_digit:
        print("Password must consist only of letters and digits")
    if count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password_validator(input())

