flag = True

while flag:
    age = input("请问您的年龄是多少？")
    if age == "quit":
        flag = False
    elif int(age) < 3:
        print("您好，这个年龄免费入场。")
    elif int(age) <= 12:
        print("您好，这个年龄票价10美元。")
    elif int(age) > 12:
        print("您好，这个年龄票价15美元。")