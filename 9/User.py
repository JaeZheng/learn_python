class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.last_name+"·"+self.first_name+", 今年"+self.age+"岁."
              + "已尝试登录" + str(self.login_attempts) + "次.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["能进入后台数据库", "能修改密码"]

    def show_privileges(self):
        print("管理员权限：")
        for privilege in self.privileges:
            print("\t" + privilege)