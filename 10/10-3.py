flag = True
file_name = "guest.txt"
while flag:
    name = input("你好访客，请问你的名字是？(输入‘q’马上退出)")
    if name == "q":
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(name.title()+"\n")
