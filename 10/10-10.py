import os


def count_words(word, file_name):
    try:
        with open(file_name, encoding='UTF-8') as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("你好，文件" + file_name + "不存在于当前目录。")
    else:
        num_of_word = 0
        for line in lines:
            num_of_word = line.lower().count(word) + num_of_word
        return num_of_word


path = os.getcwd() + "\\book\\"
file_list = os.listdir(path)
for file in file_list:
    num = count_words("the", path + file)
    print("文件"+file+"中有单词‘the’"+str(num)+"个。")