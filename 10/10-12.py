import json

file_name = "favorite_number.json"

def get_stored_number():
    try:
        with open(file_name) as json_obj:
            number = json.load(json_obj)
    except FileNotFoundError:
        print("你好，文件" + file_name + "不存在于当前目录。")
        return None
    else:
        return number


def get_new_favorite_number():
    try:
        number = input("请输入你最喜欢的一个数字：")
        number = int(number)
        with open(file_name, 'w') as json_obj:
            json.dump(number, json_obj)
    except ValueError:
        print("输入类型不为数字，请重新运行。")
    else:
        return number


def guess_fav_number():
    fav_number = get_stored_number()
    if fav_number:
        print("我知道了，你最喜欢的数字是" + str(fav_number))
    else:
        fav_number = get_new_favorite_number()
        print("我知道了，你最喜欢的数字是" + str(fav_number))


guess_fav_number()