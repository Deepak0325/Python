#q1
def filter_list(list_):
    """This function will take the list and will return the list with only integer values"""
    list_int=[]
    for i in list_:
        if type(i)==int:
            list_int.append(i)
    return list_int
print(filter_list(["hello","bye",1,2,3]))

#q2
def reverser(string_):
    """This function will string as an argument and will return the list of that string"""
    list_=list(string_)
    s=[]
    for i in list_:
        if i.islower()==True:
            s.append(i.upper())
        elif i==" ":
            s.append(i)
        elif i.isupper()==True:
            s.append(i.lower())
    return "".join(s[::-1])

print(reverser("Hello World"))

#q3
first,*middle,last=[1,2,3,4,5,6]
print(first)
print(middle)
print(last)

#q4
def factorial(a):
    output=1
    if int(a)>0:
        output=int(a)*factorial(int(a)-1)
        return output
    elif int(a)==0:
        return output
    if int(a)<0:
        print("Please pass a valid input")

print(factorial(5))

#q5
def move_to_end(list_,mover):
    list_output=[]
    for i in list_:
        if i !=mover:
            list_output.append(i)
    for j in list_:
        if j==mover:
            list_output.append(j)
    return list_output

print(move_to_end([1,2,3,1,1,1,1,5,6,6,],1))
print(move_to_end(["a","a","a","b"],"a"))