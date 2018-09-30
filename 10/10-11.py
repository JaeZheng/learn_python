import json

number = input("请输入你最喜欢的一个数字：")
file_name = "number.json"
with open(file_name, 'w') as json_obj:
    json.dump(number, json_obj)

with open(file_name) as json_obj:
    fav_number = json.load(json_obj)

print("我知道了，你最喜欢的数字是" + str(fav_number))