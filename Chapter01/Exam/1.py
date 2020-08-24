strings = "Hello World"
num = eval(input())
temp = 1
if num == 0:
    print(strings)
elif num < 0:
    for n in strings:
        print(n)
elif num > 0:
    for n in strings:
        if temp % 2 == 0:
            print(n)
            temp += 1
        else:
            print(n, end="")
            temp += 1
