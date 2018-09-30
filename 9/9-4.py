class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("********")
        print("餐厅名字：" + self.restaurant_name)
        print("菜系：" + self.cuisine_type)
        print("有" + str(self.number_served) + "人在这家餐厅就餐过")
        print("********")

    @staticmethod
    def open_restaurant():
        print("餐厅正在营业中")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


rest = Restaurant("高新街", "粤菜")
rest.open_restaurant()
rest.set_number_served(76)
rest.describe_restaurant()
rest.increment_number_served(10)
rest.describe_restaurant()
rest.increment_number_served(10)
rest.describe_restaurant()
