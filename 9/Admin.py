from UserNew import User


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