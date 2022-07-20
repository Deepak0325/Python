#q1
class div:
    def num_divisible(self,num):
        self.num=num
        """ This method will yield the numbers divisible by 7 in range 0 to {num} and upper bound is included """
        for i in range(self.num+1):
            if i%7==0:
                yield i

#Example
a=div()
b=a.num_divisible(50)

for j in b:
    print(j)

#q2
def order(a):
    """This function will take a string and will return the frequency of the words in that string"""
    l=a.split()
    l1 = list(set(l))
    z = dict()
    for i in l1:
        z[i] = l.count(i)
    for j,k in z.items():
        print(f"{j} : {k}")
order("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

#q3
"""Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class."""
class Person:
    def getGender(self):
        pass
class Male(Person):
    def getGender(self):
        print("Male")
class Female(Person):
    def getGender(self):
        print("Female")
a=Male()
a.getGender()
b=Female()
b.getGender()

#q4
subject=["I","You"]
verb=["Play","Love"]
object_=["Hockey","Football"]
def prog():
    for i in subject:
        for j in verb:
            for k in object_:
                print(f"{i} {j} {k}")
prog()

#q5
def compress(string):
    compressed_str = ""

    count = 1

    # Add in first character
    compressed_str=compressed_str+ string[0]

    # Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if (string[i] == string[i + 1]):
            count =count+ 1
        else:
            compressed_str = compressed_str+str(count)
            compressed_str =compressed_str+ string[i + 1]
            count = 1
        if string[i+1]==string[-1] and string[-1]!=string[-2]:
            compressed_str=compressed_str+str(1)
    # print last one
    if (count > 1):
        compressed_str =compressed_str + str(count)
        if string[-2]==string[-1]:
            pass
        else:
            compressed_str =compressed_str+ string[i + 1]
    return compressed_str
print(compress("hello world!hello world!hello world!hello world!"))
def decompress(string):
    l=[]
    for i in range(0,len(string),2):
        l.append(string[i]*int(string[i+1]))
    return "".join(l)
print(decompress("h1e1l2o1 1w1o1r1l1d1!1h1e1l2o1 1w1o1r1l1d1!1h1e1l2o1 1w1o1r1l1d1!1h1e1l2o1 1w1o1r1l1d1"))

#q6
def bin_search(list_,search_item):
    list_.sort(key=ascii)
    print(list_.index(search_item))
