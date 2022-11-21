def loading_bar(number):
    x = int(number / 10)
    loading = ""
    for i in range(x):
        loading += "%"
    for k in range(10 - x):
        loading += "."

    if number != 100:
        print(f"{number}% [{loading}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{loading}]")


loading_bar(int(input()))