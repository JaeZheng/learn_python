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

