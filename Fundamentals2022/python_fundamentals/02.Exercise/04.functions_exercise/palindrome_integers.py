def palindrome(x):
    list1 = []
    for i in x:
        for k in str(i):
            list1.append(k)
        list2 = list1.copy()
        list2.reverse()
        if list1 == list2:
            print("True")
        else:
            print("False")
        list1 = []


palindrome(input().split(", "))