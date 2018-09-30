dict = {
    "nile": "egypt",
    "changjiang river": "china",
    "yellow river": "china"
}
for key, value in dict.items():
    print("The "+key.title()+
          " runs through "+
          value.title())

for key in set(dict.keys()):
    print(key.title())

for value in set(dict.values()):
    print(value.title())