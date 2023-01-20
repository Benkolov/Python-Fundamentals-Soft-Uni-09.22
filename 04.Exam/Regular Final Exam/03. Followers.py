
info_followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(": ")

    if command[0] == "New follower":
        username = command[1]
        if username not in info_followers:
            info_followers[username] = {"likes": 0, "comments": 0}

    elif command[0] == "Like":
        username = command[1]
        count = int(command[2])
        if username not in info_followers:
            info_followers[username] = {"likes": 0, "comments": 0}
            info_followers[username]["likes"] += count
        else:
            info_followers[username]["likes"] += count

    elif command[0] == "Comment":
        username = command[1]
        if username not in info_followers:
            info_followers[username] = {"likes": 0, "comments": 0}
            info_followers[username]["comments"] += 1
        else:
            info_followers[username]["comments"] += 1

    elif command[0] == "Blocked":
        username = command[1]
        if username not in info_followers:
            print(f"{username} doesn't exist.")
        else:
            del info_followers[username]

print(f"{len(info_followers.keys())} followers")
for user, data in info_followers.items():
    print(f"{user}: {data['likes'] + data['comments']}")