strings = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a ** 4 + b ** 4 + c ** 4 + d ** 4 <= 1000:
                    continue
                if a ** 4 + b ** 4 + c ** 4 + d ** 4 == a * 1000 + b * 100 + c * 10 + d:
                    result = a ** 4 + b ** 4 + c ** 4 + d ** 4
                    strings.append(result)
                elif a ** 4 + b ** 4 + c ** 4 >= 10000:
                    break
                else:
                    continue

for strs in strings:
    print(strs)
