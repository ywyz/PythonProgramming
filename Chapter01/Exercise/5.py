num = input()
if num[0:3] == "USD":
    result = eval(num[3:]) * 6.78
    print("RMB{:.2f}".format(result))
elif num[0:3] == "RMB":
    result = eval(num[3:]) / 6.78
    print("USD{:.2f}".format(result))
