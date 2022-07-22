#q1
"""Escape characters are those characters which are the part of the code but that characters are not visible in the result, instead they have certain functionalities.Examples '\n' is used in the string to get a new line"""

#q2
""" n stands for new line and t stands for tab """

# example of escape character n
print("Hello world \n I am deepak")

# example of escape character t
print("Hello wo\trld")

#q3
"""We can use double backslash instead of single backslash"""
#Example
print("hello world\\")

#q4
"Howl's Moving Castle"
"""As we know we can create a string with single quote(' '), double quote(" ") and triple quote as well (''' '''). 
In the above example string is intialised by double quotes and in double quotes we can use single quotes as many times as we want"""

#q5
""" If you want to write string with new lines without passing escape character '\n', then we can use triple quotes. """
#Example
print('''Hello World
I am deepak ''')

#q6
"""
1.'e'
2.'hello'
3.'hello'
4.'lo,world!' 
"""

#q7
"""
1. 'HELLO'
2. True
3. 'hello' 
"""

#q8.1
""" It will get split on the basis of space between each word and will get stored inside a list word wise"""
'Remember, remember, the fifth of July.'.split()

#q8.2
"""'By default .split() will split the string on the basis of space between words in the string and convert it into list of words separated by comma(,) and then' "-".join()' will convert the list into string again in which words are separated by hyphen(-)"""
'-'.join('There can only one.'.split())

#q9
""" We can right justify,left justify and center the given string with the builtin methods ljust,rjust and center respectively.
It will give spaces based on the difference between specified argument and length of the string"""
#Example-Right justify. Here it will give (20-11) that is 9 spaces
"hello world".rjust(20)

#Example-left justify.Here it will give (20-11) that is 9 spaces
"hello world".ljust(20)

#Example-center.Here it will give (20-11) that is 9 spaces
"hello world".center(20)

#q10
""" we can use .strip() method available in string to remove empty spaces from start or end"""
#Example-
print("      hello       ".strip())