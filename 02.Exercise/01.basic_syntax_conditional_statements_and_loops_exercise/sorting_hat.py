command = input()

welcome = True

while command != "Welcome!":

    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6 and command != "Voldemort":
        print(f"{command} goes to Hufflepuff.")
    elif command == "Voldemort":
        print("You must not speak of that name!")
        welcome = False
        break

    command = input()

if welcome:
    print("Welcome to Hogwarts.")