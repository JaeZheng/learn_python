# -*- coding:'utf-8' -*-
with open("learning_python") as file_object:
    content = file_object.read()
    print(content)

with open("learning_python") as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open("learning_python") as file_object:
    lines = file_object.readlines()
python_string = ""
for line in lines:
    python_string += line
print(python_string.rstrip())
print(len(python_string))