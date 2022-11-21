command = input()

number_coffee = 0

while command != "END":

    # if command == "coding" or command == "dog" or command == "cat" or command == "movie":
    #     number_coffee += 1
    # elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
    #     number_coffee += 2

    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            number_coffee += 1
        else:
            number_coffee += 2
    command = input()


if number_coffee > 5:
    print("You need extra sleep")
else:
    print(f"{number_coffee}")

