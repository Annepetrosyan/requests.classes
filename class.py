# class Dict:
    
    # def __init__(self, text):
        # self.text = text
        # a = {}
        # for i in text:
            # a[i] = 1
        # print(a)
    
# text_1 = Dict("python")
        
#2 a method which returns a version of the dict without duplicate values
class NoDuplicates:
    
    def __init__(self, dict_):
        self.dict_ = dict_
        a = []
        final_dict = {}
        for k, v in dict_.items():
            if v not in a:
                a.append(v)
                final_dict[k] = v
        print(final_dict)
        
dict_1 = {"k": 2, "g": 2, "h": 3}
NoDuplicates(dict_1) 
        