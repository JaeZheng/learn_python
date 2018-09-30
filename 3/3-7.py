peoples = ["Jane", "Andy", "Tom", "July"]
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print(peoples)
print("******3-4 end******")

people_not_append = peoples.pop()
print(people_not_append + " can't append dinner.")
peoples.append("Jack")
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print(peoples)
print("******3-5 end******")

print("I found a bigger dinner table.")
peoples.insert(0, "Alan")
peoples.insert(3, "Yang")
peoples.append("Cat")
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print(peoples)
print("******3-6 end******")

print("New dinner table can't arrive in time, I just can invite two person for dinner.")
while len(peoples) > 2:
    people_reject = peoples.pop()
    print("Sorry, " + people_reject)
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
del peoples[0]
del peoples[0]
print(peoples)
print("******3-7 end******")