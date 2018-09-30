peoples = ["Jane", "Andy", "Tom", "July"]
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print("******3-4 end******")

people_not_append = peoples.pop()
print(people_not_append + " can't append dinner.")
peoples.append("Jack")
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print("******3-5 end******")

print("I found a bigger dinner table.")
peoples.insert(0, "Alan")
peoples.insert(3, "Yang")
peoples.append("Cat")
for people in peoples:
    print(people.title() + ", I invite you for dinner.")
print("******3-6 end******")