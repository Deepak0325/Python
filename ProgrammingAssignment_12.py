#q1
def unique_dict_values(dict_inp):
    """This function will return the unique values from a dictionary"""
    list_unique_values=[]
    for i in dict_inp.values():
        list_unique_values.append(i)
    return list(set(list_unique_values))

print(unique_dict_values({"a":1,"b":2,"c":3,"d":3}))

#q2
def sum_dict_items(dict_inp):
    """This function will return the sum of all items"""
    list_num_items=[]
    try:
        for i,j in dict_inp.items():
            if type(i)==int or type(i)==float:
                list_num_items.append(i)
            elif type(j)==int or type(j)==float:
                list_num_items.append(j)
    except Exception as e:
        print(e)
    return sum(list_num_items)

print(sum_dict_items({"a":1,"b":2,"c":3,"d":3}))

#q3
def merge_2_dict(dict_inp1,dict_inp2):
    """This function will merge 2 dictionaries"""
    merged_dict={}
    try:
        if type(dict_inp1)==dict and type(dict_inp2)==dict:
            merged_dict=dict(**dict_inp1,**dict_inp2)
    except Exception as e:
        return e
    return merged_dict

print(merge_2_dict({"a":1,"b":2,"c":3,"d":3},{"f":100000}))

#q4
def list_to_flat_dict(list_inp):
    dict_=dict(list_inp)
    return dict_

print(list_to_flat_dict([(1,2),("a","b"),("c","d")]))

#q5
from collections import OrderedDict

def insert_in_ordered_dict(dict_,key_value_insert):
    """This function will take 2 arguments first is dict and second is a tuple of key and value in (key,Value) form"""
    dict_=OrderedDict(dict_)
    list_=[]
    for i, j in dict_.items():
        list_.append((i, j))
    list_.insert(0,key_value_insert)
    dict_=OrderedDict(list_)
    return dict_
print(insert_in_ordered_dict({"Name":"Deepak","Age":20,"Profession":"Student"},("Phone No.",123456)))

#q6
from collections import OrderedDict
dict_={"d":4,"a":1,"e":5,"c":3,"b":2}
list_=[]
# We have to order this dict based on the values of key
for i,j in dict_.items():
    list_.append((i,j))
list_.sort()
ord_dict=OrderedDict(dict(list_))
print(ord_dict)

#q7
dict_1={"d":4,"a":7,"e":5,"c":3,"b":2}
list_1=[]
list_2=[]
for i,j in dict_1.items():
    list_1.append((i,j))
#sorting based on keys of dict
list_1.sort()
dict_1=dict(list_1)
print(dict_1)

#sorting based on values of dict
list_1.sort(key=lambda x:x[1])
dict_1=dict(list_1)
print(dict_1)