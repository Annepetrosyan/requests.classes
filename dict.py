# d = {"Anna": 23, "Gag": 24}
# print (d)
# d["Nar"] = 52
# print(d)
# print(len(d))
# print(d["Anna"])
# d[10] = 20
# print(d)
# for key, value in d.items():
    # print(f"key {key}, value {value}" )

# a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# d = {}
# cs = None
# for i in a:
    # if type(i) is str:
        # d[i] = []
        # cs = i
    # else:
        # d[cs].append(i)
        
# print(d)

#1. exercise
# text = input("Write a text \n " ) 
# def reversed_txt(text: str) -> str:
    # return " ".join(text.split()[: : -1])
     
    
# print(reversed_txt(text))

#3   
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict4={6:50,7:60}
# final_dict = {**dict1, **dict2, **dict3, **dict4}
# print(final_dict)
                                       
#2

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# def list_(k,v: list) -> list:
    # for i in k:
        # if i in b and i not in c:
            # c.append(i)
    # return c
        
# print(list_(a , b)) 

#4
# n = int(input("input the number which will be appeared in dictionary \n"))
# dict = {}

# for x in range(1, n+1):
    # dict[x] = x ** 2
# print(f"the square of numbers from 1 to the number you have mentioned is \n {dict}")


# try:
    # n = int(input("input the number which will be appeared in dictionary \n"))
    # dict = {}
    # for x in range(1, n+1):
        # dict[x] = x ** 2
    # print(f"the square of numbers from 1 to the number you have mentioned is \n {dict}")
    
# except ValueError:
    # print("Please enter an integer!")
    
# finally:
    # print("Thank you for using our program")
    
    
#5

original_dict = {"c1": "Red", "c2": "Green", "c3": None, "c4": None} 
final_dict = {}
for k, v in original_dict.items():
    if v is not None:
        final_dict[k] = v
print(final_dict)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















    