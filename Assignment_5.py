#q1 What does an empty dictionary's code look like?
dict_=dict()
#or
dict1={}

#q2
value={"foo":42}


#q3
"""Main distinction between list and dictionary is that dictionary is that dictionaries are created with curly braces ({}) and lists are created with square brackets([])."""

#q4
"""We will get keyError."""

spam={"bar":100}
#spam["foo"]

#q5
"""There is no difference because by default the 1st statement checks "cat" in keys of dictionary(spam) and in  the 2nd statement we have already specified to check in the keys."""

#q6
"""As we know dictionary exists in form of key-value pair. Therefore, there is a difference between key and value.
Yes, there is difference in the results we will get because by default the 1st statement checks "cat" in keys of dictionary(spam) and in the second statement it will check "cat" in values of dictionary(spam)."""

#q7
spam={}
spam.setdefault('color','black')
print(spam)
#q8
dict_={"foo":" bar","name":{"deepak":"chanana","sudhanshu":"kumar","krish":"naik"}}

import pprint  # Importing the pprint module

pprint.pprint(dict_)

#Using pprint module and the function name is also pprint.