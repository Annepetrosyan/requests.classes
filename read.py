import os
cwd = os.getcwd()
file_path = os.path.join(cwd, "sample.txt")


##1
#
# file = open("sample.txt", "r")
# counter = 0
#
# content = file.read()
# c = content.split("\n")
#
# for i in c:
#     if i:
#         counter += 1
#
# print(f"the number of lines is equal to  {counter}")

##2
#
# def foo(file_name, letter):
#     file = open(file_name, 'r')
#     text = file.read()
#     return text.count(letter)
#
# print(foo("sample.txt", "<<"))

##3
import re
file = open("sample.txt", "r")
content = file.read()
a = re.findall("<.*?>.", content)

print(a)



##4
#
# file = open("sample.txt", "r")
# file_1 = open("bn.txt", "a")
#
#
#
# content = file.read()
# c = content.split("\n")
#
# for i in c:
#     if not i.isdigit():
#         file_1.write(f"{i}, \n")


