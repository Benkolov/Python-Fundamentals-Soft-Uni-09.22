text = input().split()
final_text = [word for word in text if len(word) % 2 == 0]
print('\n'.join(final_text))
