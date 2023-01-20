import re

number = int(input())

for i in range(number):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]+[A-Z])(\@\#+)'
    result = re.match(pattern, data)

    if result is None or len(result.group()) < 10:
        print("Invalid barcode")
    else:
        extract_nums = re.findall(r'\d', result.group())

        if not extract_nums:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")