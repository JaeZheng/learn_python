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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, ice_cream):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream = ice_cream

    def describe_ice_cream(self):
        print("有以下品种的冰淇淋：")
        for item in self.ice_cream:
            print(item)


ice_list = ["巧克力冰淇淋", "香草冰淇淋", "菠萝冰淇淋"]
temp = IceCreamStand("米其林", "甜品", ice_list)
temp.describe_restaurant()
temp.describe_ice_cream()