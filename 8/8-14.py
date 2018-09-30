def make_car(type, size, **car_info):
    car = {}
    car['品牌'] = type
    car['型号'] = size
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car("夏利", "低配型", color="绿色")
print(car)
car = make_car("宝马", "高配型", color="白色", output="2.4L")
print(car)
