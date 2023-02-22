import re

# pattern = r"(?P<surr>=|/)([A-Za-z]{3,})(?P=surr)"
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
text = input()
matches = re.finditer(pattern, text)
number = 0
country = []
for match in matches:
    a = match[2]
    country.append(a)
    number += len(a)

print(f"Destinations: {', '.join(country)}")
print(f"Travel Points: {number}")

