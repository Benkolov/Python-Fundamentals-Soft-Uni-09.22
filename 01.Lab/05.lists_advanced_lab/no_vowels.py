vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
no_vowels_text = [i for i in text if i not in vowels]

print(''.join(no_vowels_text))