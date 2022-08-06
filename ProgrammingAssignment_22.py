# q1
def list_operation(a, b, c):
    """this function will return the elements from a to b which are divisible by c"""
    list_ = []
    for i in range(a, b + 1):
        if i % c == 0:
            list_.append(i)
        else:
            pass
    return list_


list_operation(1, 10, 3)


# q2
def simon_says(a, b):
    """ this function will return True or False based upon the second list(b) if it follows the first list(a) by 1"""
    try:
        for i in range(int(len(a))):
            if a[i] == b[i + 1]:
                return True
            else:
                return False
    except Exception as e:
        return e


print(simon_says([1, 2], [2, 1]))

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))


# q3
def society_name(a):
    """ This function will return the name of the secret society based upon the values inside the list"""
    initials_list = []
    for i in a:
        initials_list.append(i[0])
    initials_list.sort()
    return "".join(initials_list)


society_name(["Harry", "Newt", "Luna", "Cho"])


# q4
def is_isogram(a):
    try:
        if " " in a:
            return (" Please pass 1 word string")
        if len(list(str(a).lower())) == len(set(list(str(a).lower()))):
            return True

        else:
            return False
    except Exception as e:
        return e


is_isogram("PasSword")

is_isogram("Algorism")


# q5
def is_in_order(a):
    list_ = list(a)
    list_1 = []
    try:
        if len(a) == 0:
            print("Encountered a string with length 0 please pass a valid string")
        else:
            for i in list_:
                list_1.append(ord(i))
            if list_1 == sorted(list_1):
                print(True)
            else:
                print(False)
    except Exception as e:
        print(e)


is_in_order("abzz")

is_in_order("")

