import time
import datetime
flag = True
file_name = "guest_book.txt"
while flag:
    name = input("你好访客，请问你的名字是？(输入‘q’马上退出)")
    if name == "q":
        break
    else:
        print("你好，" + name.title() + "，欢迎访问系统。")
        date = datetime.date.today()
        now = time.strftime("%H:%M:%S")
        with open(file_name, 'a') as file_object:
            file_object.write(name.title() + "在" + str(date)
                              + " " + str(now) + "访问系统。\n")
