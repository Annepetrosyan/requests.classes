def __init__(self, dict_):
    self.dict_ = dict_
    a = []
    final_dict = {}
    for k, v in dict_.items():
        if v not in a:
            a.append(v)
            final_dict[key] = v
        

    