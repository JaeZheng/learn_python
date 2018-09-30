from collections import OrderedDict

favorite_places = OrderedDict()
favorite_places["Jae"] = ["Beijing", "NewYork"]
favorite_places["Jason"] = ["Nanjing", "Guangzhou"]
favorite_places["Chely"] = ["Shanghai"]
for person, places in favorite_places.items():
    print(person + " like places:", end=" ")
    for place in places:
        print(place, end=" ")
    print()