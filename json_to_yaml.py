import os
import json
from json import JSONEncoder
from json import JSONDecoder
import yaml

# # open("json_1.json", "a")
# json_file = os.path.join(os.getcwd(), "json_1.json")
#
#
# # a = dict(
# #     name = "Anna",
# #     surname = "Smith",
# #     age = 23
# # )
# #
# # with open (json_file, "w") as f:
# #     json.dump(a, f)
# def foo():
#     with open (json_file, "r") as f:
#         data =  json.load(f)
#         # print(data)
#
#     # open("yaml_1.yaml", "a")
#
#     yaml_file = os.path.join(os.getcwd(), "yaml_1.yaml")
#     with open (yaml_file, "w") as ff:
#         yaml.dump(data, ff)
#
#
# foo()





# def foo():
#     yaml_file = os.path.join(os.getcwd(), "yaml_1.yaml")
#     with open(yaml_file, "r") as ff:
#        data = yaml.safe_load(ff)
#
#
#     json_file = os.path.join(os.getcwd(), "json_1.json")
#     with open (json_file, "w") as f:
#         json.dump(data, f)
#
#
#
#
# foo()




# def yaml_to_text():
#     yaml_file = os.path.join(os.getcwd(), "yaml_1.yaml")
#     with open(yaml_file, "r") as file:
#         data = yaml.safe_load(file)
#        # print(data)
#
#
#
#     text_file = os.path.join(os.getcwd(), "text.txt")
#
#
#     with open(text_file, "w") as f:
#         f.write(str(data))
#
# yaml_to_text()



def text_to_json():
    json_file = os.path.join(os.getcwd(), "json_1.json")
    with open("text.txt", "r") as f:
        data = f.read()
    with open(json_file, "w") as ff:
        json.dump(data, ff)

text_to_json()