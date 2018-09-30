my_pizzas = ["Pan Pizza", "Hand-tossed Style Pizza", "California Style Pizza"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Chicago Style Pizza")
friend_pizzas.append("Cracker and Thin Styles Pizza")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)