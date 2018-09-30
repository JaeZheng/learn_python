class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self.last_name+"·"+self.first_name+", 今年"+self.age+"岁.")


def greet_user(user):
    print("你好，"+user.age+"岁的"+user.last_name+"·"+user.first_name+"!")


user_jae = User("郑", "家伟", "21")
user_yelo = User("黄", "纯", "22")

user_jae.describe_user()
user_yelo.describe_user()

greet_user(user_jae)
greet_user(user_yelo)