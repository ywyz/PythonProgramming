result = 0
for i in range(967):
    if i % 2 == 0:
        result -= i

    else:
        result += i
print(result)