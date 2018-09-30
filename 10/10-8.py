file_name = "dogs.txt"
try:
    with open(file_name) as file_object:
        for line in file_object:
            print(line.rstrip())
except FileNotFoundError:
    print("你好，文件"+file_name+"不存在于当前目录。")