# # 1 write a python program to remove duplicated nested lists from a list

# def filtered_(a: list) -> list:
     # for l in a:
         # if a.count(l) > 1:
           # a.remove(l) 
            # return a 
           
 # b = [[10, 20], [30, 56, 25], [10, 20], [33], [40]]
 # print(filtered_(b))
            



def flatten(list_: list) -> list:
    flatten_list = []
    for i in list_:
        if i is int:
            flatten_list.append(i)
        if i is list:
            for item in i:
                flatten_list.append(item)
                
            return flatten_list

original_list =  [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]       
print(flatten(original_list))
        