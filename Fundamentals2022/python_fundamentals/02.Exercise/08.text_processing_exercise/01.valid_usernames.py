user_name = input().split(", ")

for name in user_name:
    username_is_valid = True
    if not 3 <= len(name) <= 16:
        username_is_valid = False
    for char in name:
        if not(char.isalnum() or char == "-" or char == "_"):
            username_is_valid = False
    if " " in name:
        username_is_valid = False
    if username_is_valid:
        print(name)
