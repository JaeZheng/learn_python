class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("********")
        print("餐厅名字：" + self.restaurant_name)
        print("菜系：" + self.cuisine_type)
        print("********")

    @staticmethod
    def open_restaurant():
        print("餐厅正在营业中")


rest = Restaurant("高新街", "粤菜")
rest.open_restaurant()
rest.describe_restaurant()
