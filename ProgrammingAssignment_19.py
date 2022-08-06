#q1
def double_char(a):
  """ This function will take the input as a string and will return the string with every character of string repeated once"""
  l=[]
  for i in a:
    l.append(2*i)
  return "".join(l)

print(double_char("string"))

#q2
def reverse_(a):
  """ This function will return the reverse of boolean value"""
  try:
    if type(a)!=bool:
      return "boolean expected"
    else:
      if a==True:
        return False
      elif a==False:
        return True
      else:
        pass
  except Exception as e:
    return e

print(reverse_(0))

print(reverse_(True))

print(reverse_(False))

#q3
def num_layers(a):
  """ This function will return the thickness of paper after passing the number of folds"""
  k=((2**a)*0.5)/1000
  return (f"{k} m")

num_layers(21)


#q4
def index_of_caps(a):
  """ This fucntion will return the index of all capital case letters in a string"""
  list_index_caps=[]
  for i in a:
    if ord(i)<97:
      list_index_caps.append(a.index(i))
  return list_index_caps

print(index_of_caps("eDaBiT"))

print(index_of_caps("determine"))

#q5
def find_even_nums(x):
  """ This function will return the even numbers from 1 to x"""
  list_even_nums=[x for x in range(1,x+1) if x%2==0 ]
  return list_even_nums

print(find_even_nums(8))

print(find_even_nums(4))