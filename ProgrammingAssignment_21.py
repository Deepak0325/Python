#q1
def next_in_line(a,b):
  """ This function will take 2 arguments a is list and b is an integer and this function will delete the first element and add b in the last."""
  a=a
  try:
    if type(a)!= list:
      print("Pass the valid argument a should be a list and b should be an integer")
    elif len(a)==0:
      print("No list has been selected")
    elif type(a)==list:
      a.pop(0)
      a.append(b)
      return a
  except Exception as e:
    return e


print(next_in_line([5,6,7,8,9],1))

#q2
def get_budgets(a):
  """ this function will take list as an argument and within list there will be multiple dictionaries and this function will return the sum of budget."""
  list_of_budget=[]
  try:
    if len(a)==0:
      print("length of list is 0 please pass a valid argument")
    else:
      for i in a:
        for j,k in i.items():
          if j=="budget":
            list_of_budget.append(k)
      return sum(list_of_budget)
  except Exception as e:
    return e


get_budgets([
{"name":"John","age":21,"budget":23000},
{"name":"steve","age":32,"budget":40000},
{"name":"Martin","age":16,"budget":2700}
])

#q3
def alphabet_soup(a):
  """ this function will return the string in the alphabetical order"""
  a=a
  try:
    if len(a)==0:
      return("length of string is 0 please pass a valid string")
    else:
      list_=list(a)
      list_.sort(key=ascii)
    return "".join(list_)
  except Exception as e:
    return e


print(alphabet_soup("hello"))

print(alphabet_soup("javascript"))

print(alphabet_soup(""))

#q4
def compound_interest(p,t,r,n):
  """ This function will give you the compound interest p= Principal Amount, t= No.of years, r= Rate of interest(please pass this argument with decimal and %symbol) n= no.of compounding periods per year"""
  p=p
  t=t
  r=r/100
  n=n
  middle_part=1+r/n
  power_=t*n
  middpower=middle_part**power_
  try:
      if p==0 or t==0 or r==0 or n==0:
        return ("Please pass a valid input")
      else:
        return round((p*middpower),2)
  except Exception as e:
      return e



print(compound_interest(10000,10,6,12))

#q5
def return_only_integer(a):
  """ this function will take input as list and will return integers inside a list"""
  only_int=[]
  try:
    if type(a)!=list:
      return "list not given"
    elif len(a)==0:
      return "length of list is 0"
    else:
      if type(a)==list:
        for i in a:
          if type(i)==int:
            only_int.append(i)
          else:
            pass
      return only_int
  except Exception as e:
    return e

print(return_only_integer([1,2,3,45,"asdf",True,22.2]))