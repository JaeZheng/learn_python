flag = True
while flag:
    message = input("请输入一种披萨配料(输入quit时退出): ")
    if message == "quit":
        flag = False
    else:
        print(message + "已加入。")