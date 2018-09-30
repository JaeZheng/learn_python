with open("learning_python") as file_object:
    lines = file_object.readlines()
    print(len(lines))
python_string = ""
for line in lines:
    python_string += line
new_string = python_string.replace("Python", "C++")
print(new_string.rstrip())