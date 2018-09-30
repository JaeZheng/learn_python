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


user_kobe = User("Kobe", "Bryant", "21")
user_kobe.describe_user()
user_kobe.increment_login_attempts()
user_kobe.increment_login_attempts()
user_kobe.increment_login_attempts()
user_kobe.increment_login_attempts()
user_kobe.describe_user()
user_kobe.reset_login_attempts()
user_kobe.describe_user()

