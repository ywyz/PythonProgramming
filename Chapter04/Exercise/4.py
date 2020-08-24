strings = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            if a ** 3 + b ** 3 + c ** 3 <= 100:
                continue
            if a ** 3 + b ** 3 + c ** 3 == a * 100 + b * 10 + c:
                result = a ** 3 + b ** 3 + c ** 3
                strings.append(result)
            elif a ** 3 + b ** 3 + c ** 3 >= 1000:
                break
            else:
                continue
length = len(strings)
for strs in strings:
    print(strs, end="")
    length -= 1
    if length > 0:
        print("", end=",")