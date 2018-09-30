try:
    print("加法运算：")
    num_1 = input("请输入第1个数：")
    num_1 = int(num_1)
    num_2 = input("请输入第2个数：")
    num_2 = int(num_2)
    print("两个数字之和为：" + str(num_1+num_2))
except ValueError:
    print("输入类型不为数字，请重新运行。")