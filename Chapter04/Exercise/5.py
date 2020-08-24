error = 0
names = "Kate"
passwords = "666666"

for i in range(3):

    iuput_name = input()
    input_passwords = input()
    if iuput_name == names:
        if input_passwords == passwords:
            print("登录成功！")
            break
        else:
            error += 1
            if error == 3:
                print("3次用户名或者密码均有误！退出程序。")
            continue
    else:
        error += 1
        if error == 3:
            print("3次用户名或者密码均有误！退出程序。")
        continue
