n = int(input())

pianist_data = {}

for i in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]

    pianist_data[piece] = {'composer': composer, 'key': key}


while True:
    command = input().split('|')
    if command[0] == "Stop":
        break
    piece = command[1]

    if command[0] == "Add":
        composer = command[2]
        key = command[3]

        if piece not in pianist_data:
            pianist_data[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        if piece in pianist_data:
            del pianist_data[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in pianist_data:
            pianist_data[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


for piece, data in pianist_data.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")