l=["abhi","ram","venugopal"]

def len_string(str_list):
    return [len(i) for i in str_list]

print(len_string(l))

print(len(max(l,key=len)))