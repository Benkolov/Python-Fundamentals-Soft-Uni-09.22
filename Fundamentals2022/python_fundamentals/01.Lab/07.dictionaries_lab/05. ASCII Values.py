# print({char: ord(char) for char in input().split(', ')})

list_of_characters = input().split(", ")
characters = {key: ord(key) for key in list_of_characters}
print(characters)