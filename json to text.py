import os
import json
from json import JSONEncoder
from json import JSONDecoder




a = dict(
    name = "Anna",
    surname = "Smith",
    age = 23
)

json_file = os.path.join(os.getcwd(), "new_file.json")

with open(json_file, "w") as file:
    json.dump(a, file)

def foo():
    with open(json_file, "r") as file:
        data = json.load(file)
        print(data)




    text_file = os.path.join(os.getcwd(), "text.txt")


    with open(text_file, "w") as f:
        f.write(str(data))

foo()








# with open('new_file.json', 'r') as f:
#     data = json.loads(f)