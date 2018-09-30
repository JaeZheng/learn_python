pizzas = ["Pan Pizza", "Hand-tossed Style Pizza", "California Style Pizza",
          "Thick Style Pizza", "Take and Bake Style Pizza"]
print("前三个元素是：" + str(pizzas[:3]))
middle = int(len(pizzas)/2)
print("中间的三个元素是：" + str(pizzas[middle-1:4]))
print("末尾三个元素是：" + str(pizzas[-3:]))