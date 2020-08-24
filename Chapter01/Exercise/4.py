Temperature = input()
if Temperature[0] == 'F':
    result = (eval(Temperature[1:]) - 32) / 1.8
    print("C{:.2f}".format(result))
elif Temperature[0] == 'C':
    result = eval(Temperature[1:]) * 1.8 + 32
    print("F{:.2f}".format(result))
