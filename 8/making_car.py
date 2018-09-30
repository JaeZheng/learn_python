def make_car(type, size, **car_info):
    car = {}
    car['品牌'] = type
    car['型号'] = size
    for key, value in car_info.items():
        car[key] = value
    print(car)

