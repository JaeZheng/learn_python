car_1 = "audi"
car_2 = "AUDI"
print(car_1 == car_2)
print(car_1 == car_2.lower())
num_1 = 10
num_2 = 10
print(num_1 == num_2)
num_2 = 11
print(num_1 != num_2)
print(num_2 > num_1)
print(num_1 < num_2)
print(num_2 >= num_1)
print(num_1 <= num_2)
num_3 = 9
print(num_1 < num_2 and num_1 < num_3)
print(num_1 < num_2 or num_2 < num_3)
foods = ("pizza", "carrot", "cake", "noodles", "rice")
print("pizza" in foods)
print("pizza" not in foods)