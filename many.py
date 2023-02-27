""" --> 3 double quotes or 3 single quotes can be used for multi-line comments.
These are called docstrings for multi line comments typically used in functions.
however, single quotes are reserved for documentation and double quotes for comments

IDLE comes with python installation
hit f5 to execute
to run in idle, open idle and navigate to this file
IDLE is a REPL program - read-eval-print-loop

we can also use jupyterlabs notebooks, ipynb files, to run samples from - interactive python notbeook files
from anaconda, use jupyter labs 3.2.1 as per below explanation. jupyterlabs is next generation of jupyter notebooks
there, we use shift+enter to execute each line

Note that JupyterLab has a extensible modular architecture. So in the old days, there is just one Jupyter Notebook,
and now with JupyterLab (and in the future), Notebook is just one of the core applications in JupyterLab (along
with others like code Console, command-line Terminal, and a Text Editor). JupyterLab will eventually replace the
classic Jupyter Notebook. Throughout this transition, the same notebook document format will be supported by both
the classic Notebook and JupyterLab

anaconda is basically a data science toolkit which supports numerous platforms from within it for enterprise
projects, pycharm or even eclipse looks good whereas for single file projects/data analysis or data science
proejcts, spyder looks good. navigate to http://localhost:8888/lab for jupyterlabs

IDLE is cool because it detects and wraps/folds/collapses unnecessary/long outputs automatically
-----------------------------------------------------#

everything is an object in Python. Objects have state(attributes/values) and behavior(methods)
current version - 3.10.0 -  started to learn on Dec 19th 2021, day after passing aws saa-c02
to run sample.py, use 'python sample.py'
to run directly online, we can use Google Collab, Repl it, JupyterNotebooks/JupyterLab
strings are immutable in Python.


When it comes to formatting your code (not just strings), the Python programming
community has spent a long time establishing and documenting best practice. This
best practice is known as PEP 8. PEP is shorthand for "Python Enhancement Protocol."

There are a large number of PEP documents in existence, and they primarily detail
proposed and implemented enhancements to the Python programming language,
but can also document advice (on what to do and what not to do), as well as describe
various Python processes. The details of the PEP documents can be very technical and
(often) esoteric. Thus, the vast majority of Python programmers are aware of their
existence but rarely interact with PEPs in detail. This is true of most PEPs except for PEP 8.

PEP 8 is the style guide for Python code. It is recommended reading for all Python
programmers, and it is the document that suggests the "be consistent" advice for string
quotes described on the last page. Take the time to read PEP 8 at least once. Another
document, PEP 257, offers conventions on how to format docstrings, and it's worth reading, too.

we have meta-peps, other informational peps, provisional peps, accepted peps, open peps
# -----------------------------------------------------#
"""


# -----------------------------------------------------#

# seeking_input=input('what is your name?') #for getting input from console
# print(f'Hello {seeking_input}')
# input always converts input to a string. so even if '30' is entered as input, it is stored as a string. to get the right datatype, use int(input) or float(input) etc
from main import printDelimiter #by doing this, we can use printDelimiter without any qualifications
#import main #if we did this, we needed to use main.printDelimiter everywhere.
#if we use 'from main import printDelimiter' , we cannot  use main.printDelimiter


printDelimiter('Section 01')
print(4 ** 2)  # square
print(4 ** 3)  # cubed
print(4 ** 0.5)  # square root
print(4 ** 4)  # power of
print(4 % 3) #modulo - 1

print(7//4) # 1
#The reason we get this result is because we are using "*floor*" division. The // operator (two forward slashes) truncates the decimal without rounding, and returns an integer result.

a = 2
print(type(a))

a = 'String'
print(type(a))

a = [1, 2, 3, 4, 5]  # list  is an ordered set of unstructured objects
a = {1, 2, 3, 4, 4}  # set is unordered collection of unique objects. this is ok but internally it stores only 1, 2,3,4
print(a)  # only prints 1, 2, 3, 4
a = {'k1': 1, 'L2': "3", "k3": [1, 2, 3]}  # dict is unordered key values for structured data
a = (1, 2, 3)  # tuples are ordered immutable sequence of objects.
a = False  # boolean

# ? : ternary operator is done this way in python:
y = 4
x = 10 if y > 3 else 20
print(x)

# -----------------------------------------------------#
printDelimiter('Section 02')


print("--".join(['a','b','c'])) #'a--b--c' join joins a list as a string with the provided delimiter
# print(' '.join([1,2,3])) #joining int's will result in error
print("--".join(['a','2','3']))
print("--".join(('a','2','3')))
print("--".join({'a','2','3','3'}))

print(len('Hello World'))
print('Hello World'[1]) #e
print('Hello World'[-1]) #d
print('Hello World'[:-1]) #Hello Worl
print('Hello World'[::-1])  # in reverse
print('Hello World'[::-2])  # in reverse and skip every other character
print('Hello World'[:2:])  # this is also ok, print first 2 characters
s = 'hello world'
s = s + ' concatenate me!'
print(s)
print(s * 3);  # having semi colon at the end is ok too! this prints s thrice
print(s.upper() + s.lower())
print(s.split())
print(s.split('o'))  # ['hell', ' w', 'rld c', 'ncatenate me!']
# -----------------------------------------------------#
printDelimiter('Section 03')

print("I'm going to inject %s here." % 'something')
print("I'm going to inject %s text here, and %s text here." % ('some', 'more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here." % (x, y))
print('He said his name was %s.' % 'Fred') # no single quotes - just Fred
print('He said his name was %r.' % 'Fred')  #includes single quotes like 'Fred'

# -----------------------------------------------------#
printDelimiter('Section 04')
print('Floating point numbers: %5.2f' % (13.144))
print('Floating point numbers: %1.0f' % (13.144))
print('Floating point numbers: %10.2f' % (13.144))  # adds padding if not enough numbers
print('First: %s, Second: %5.2f, Third: %r' % ('hi!', 3.1415, 'bye!'))
print('This is a string with an {}'.format('insert'))
print(f'Hi, {s}');
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1, b='Two', c=12.3))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# -----------------------------------------------------#
printDelimiter('Section 5')
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# Fruit    | Quantity
# Apples   |       3.0
# Oranges  |        10

print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right')) # < - left align, ^ - middle align, > - right align
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))
# Left     |  Center  |    Right
# 11       |    22    |       33
# -----------------------------------------------------#
printDelimiter('Section 06')
name = 'Fred'

print(f"He said his name is {name}.")
print(f"He said his name is {name!r}") #He said his name is 'Fred' - with single quotes around 'Fred'

print(len('hello'))
print('Hello World'[4:9:2]) #oWr
print('Hell'[1:]) #ell
print('Hell'[:2]) #He
print('Hell'[:-1]) #Hel
print('Hell'[::-1]) #lleH
print('Hell'[1:])
print('abcd'.upper()) #.lower,
print('Hell World'.split()) #['Hell', 'World']
print('Hell World'.split('l')) #['He', '', ' Wor', 'd']


for i in [1,2,3]:
    pass #this can be used as a placeholder as there should be something in loop or we get error
print('out of for loop')

#in addition to pass, we can also have:
#break: Breaks out of the current closest enclosing loop.
#continue: Goes to the top of the closest enclosing loop.

# -----------------------------------------------------#
printDelimiter('Section 07')

my_list = ['A string', 23, 100.232, 'o']
len(my_list)
my_list[0]
my_list[1:]
my_list = my_list + ['add new item permanently']
print(my_list * 2)
my_list.append('append me!')
my_list.pop(0)  # indexed item and also returns the item
myval = my_list.pop()  # from end
print(myval)
print(my_list)
# print(my_list[100] ) #will return in error
# we can also perform sort(), reverse() methods
my_list = [1,3,4,3,2,5,6,10,9,8,7]
my_list.reverse() #returns nothing and silently and internally reverses the items
print(my_list)
my_list.sort() # same as above
print(my_list)
print(min(my_list))
print(max(my_list))


lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]
print(matrix[0][0])
print(matrix)


# List comprehensions:
first_col = [row[0] for row in matrix]
print(first_col)
first_col = [column[0] for column in matrix]
print(first_col)

# lst_3.remove(2) #this  will result in error as lst_3 does not have 2 and remove is to remove actual value and is not an index
lst_3.remove(8)
print(lst_3)

lst_3.extend([8, 9])

lst_3.insert(2, 10)
print(lst_3)

# -----------------------------------------------------#
# Assigment operators act as pointers. we need to use copy methods to copy objects. then any subsequent modifications on copy will not impact the original
printDelimiter('Section 08')
a = [1, 2, 3, 4]
b = a
b.append('a')

c = a.copy()
c.append('b')
print(a)

a = 'a string'
b = list(a)  # to get a list from a string
print(b)

print(''.join(b))  # join is used to get string from list
print(''.join(b[0:3]))
print(''.join(b[0:3:2]))

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
#(2,4)
#(6,8)
#(10,12)

for (t1,t2) in list2:
    print(t1) #2, 6, 10

lst = [x for x in 'word']
print(lst) # the above is called 'list comprehension'. now lst will be ['w','o','r','d'].
#comprehension is where we take an empty list, iterate through a destination and append values to the list.
#Comprehensions require less code and are optimized for the interpreter. Above is example of list comprehension or listcomp for short
#then we have dictionary composition or dictcomp also and also a setcomp. there is no tuple comprehension though
#dict comp example: just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items()}
#dict comp with filters: just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
#we dont have tuple comprehensions because tuples are immutable and cannot be changed so no sense of comprehensions for them which are more dynamic


lst = [x**2 for x in range(0,11)]
print(lst) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lst = [x for x in range(11) if x % 2 == 0]
print(lst) # [0, 2, 4, 6, 8, 10]

lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst) #[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

# -----------------------------------------------------#
printDelimiter('Section 09')

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item) #k1, k2, k3.. iterates by keys by default. need to ask for items
print(d.items()) #dict_items([('k1', 1), ('k2', 2), ('k3', 3)]

for k,v in d.items():
    print(k) #k1,k2,k3
    print(v) #1,2,3
#Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():
print(sorted(d.values()))

for i in range(1,10):
    #first item d[k4] will not exist and will give error. to avoid it, we can initialize it as below. and if it is already initialized, it will not do anything
    #without it, we get KeyError if we try to access an item which doesnt have a valid key
    d.setdefault('k'+str(i), 'item')
    print(d['k'+str(i)])

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
print(my_dict['key3'][1])
my_dict['key1'] -= 123
print(my_dict['key1']) #0

#create new dictionary/dict
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])
d['key1']['nestkey']['newkey']=82
print(d) #{'key1': {'nestkey': {'subnestkey': 'value', 'newkey': 82}}}



# -----------------------------------------------------#
printDelimiter('Section 10')

t = (1,2,3,4,5)

for t1 in t:
    print(t1)

print(len(t))
print(t[0], t[-1]) #1 and 5

print(t.index(3)) #2
print(t.count(1)) #1 -- number of times 1 appears in the tuple

#similar to strings, tuples are immutable. so trying something like t[1]=3 will return in error - TypeError
# we cannot add to a tuple either with this method also t.append('nope')

a = [('a'), ('b'), ('c', 'd')]
print(a) #['a', 'b', ('c', 'd')] ?? no tuples for first 2 elements?
'''
What looks like a single-object tuple isn't; it's a string. This has happened
due to a syntactical quirk in the Python language. The rule is that, in order
for a tuple to be a tuple, every tuple needs to include at least one comma
between the parentheses, even when the tuple contains a single object. This
rule means that in order to assign a single object to a tuple (we're assigning a
string object in this instance), we need to include the trailing comma, like so
'''

#to fix above, we need weird fix as per below to include a comma at the end of the tuple list:
a = [('a',), ('b',), ('c', 'd')]
print(a, '--test')


# -----------------------------------------------------#
printDelimiter('Section 11')
x = set()
x.add(1)
x.add(2)
list1 = [1,1,2,2,3,4,5,6,1,1]
y=set(list1) # y will have only 1, 2, 3,4,5,6

print(x,',', y)

vowels2 = set('aeeiouu')
print(vowels2) #not in proper order as sets are unordered
print(sorted(vowels2)) #a e i o u now!
word='karthik'
vowels2=vowels2.union(set(word))
print(vowels2)

#difference tells whats not shared between 2 sets
print(set('aeiou').difference(set('karthik')))
#intersection tells whats common
print(set('aeiou').intersection(set('karthik')))
print(tuple("aeiou"));

# -----------------------------------------------------#
printDelimiter('Section 12')
print(1 < 2 < 3)
print(1<2 and 2<3)
print(1<2 or 4<3)

a,b=1,2
if(a > 1) :
    print('a is greater than 1')
elif(b>2) :
    print('b is greater than 2')
else:
    print('i guess it doesnt matter who is greater than who')


#range(x,y) is used to generate integers from x to y, not including y. range(x) is from 0 to x not including x
# it can take a third parameter, which is step size
print(list(range(10))) # 0 to 9
print(list(range(1,10))) # 1 to 9

print(list(range(10,1,-1))) # 10 to 2

#Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry
#about creating and updating this index_count or loop_count variable
#enumerate creates tuples for us automatically -- below creates [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


print(list(enumerate('abcde')))  #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
#zip is used to create a list of tuples:
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
print(list(zip(mylist1,mylist2))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
mylist3 = [100,200,300,400,500]
print(list(zip(mylist1,mylist2,mylist3))) #[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]
mylist3 = [100,200,300,400]
print(list(zip(mylist1,mylist2,mylist3))) # [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400)]

# -----------------------------------------------------#
printDelimiter('Section 13')
from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
# -----------------------------------------------------#
printDelimiter('Section 14')
from os import getcwd

where_am_I = getcwd()
print(where_am_I)
# -----------------------------------------------------#
printDelimiter('Section 15')
myfile = open('main.py')
print(myfile.read())
print('reading again')
print(myfile.read())  # wont print as cursor is at end of file
print('reading again and again')
myfile.seek(10)
print(myfile.read())

x = open('test.txt', 'w')
x.write('Hello World\n');
x.write('Hello World2\n');
x.close()

x = open('test.txt', 'r')
y=x.readlines()
print(y)
x.close()

#x = open('test.txt', 'w')
#y=x.read() #error as file was opened for writing

x = open('test.txt', 'w+')
y=x.read() #ok as it is write + read.. similarly, we have a+ which is append + read. we also have x which is for opening file for writing but will fail if file already exists
x.close()

x = open('test2.txt', 'a+')
print('2Put out the trash.', file=x) #output to filestream of test2.txt

for asdf in open('test2.txt'):
    print(asdf) #by reading line by line, we dont have to load entire file to memory as is done by read() method

#print appends a newline by default. use end='' to stop that
for asdf in open('test2.txt'):
    print(asdf, end='')  # by reading line by line, we dont have to load entire file to memory as is done by read() method

#by default, file opens in read mode and that too as ascii. to open as binary, use 'b' mode
for asdf in open('test2.txt', 'rb'):
    print(asdf, end='')  # by reading line by line, we dont have to load entire file to memory as is done by read() method


#Python supports “open, process, close.” But most Python programmers prefer to use the “with” statement.

with open('test2.txt') as tasks:
 for chore in tasks:
   print(chore, end='')

with open('test2.txt') as tasks:
 print(tasks.read()+"haha")

# -----------------------------------------------------#
printDelimiter('Section 16')
import sys

print(sys.platform)
print(sys.version)
# -----------------------------------------------------#
printDelimiter('Section 17')
import os

print(os.name)
# print(os.environ)
# you can use tab key to print function names automatically
print(os.getenv('HOME'))
# -----------------------------------------------------#
printDelimiter('Section 18')
import datetime

print(datetime.date.today())

datetime.date.today().day
# 31

print(datetime.date.isoformat(datetime.date.today()))
# -----------------------------------------------------#
printDelimiter('Section 19')
import time

print(time.strftime("%H:%M:%S") + '--' + time.strftime("%A %p"))

import html

print(html.escape("This HTML fragment contains a <script>script</script> tag."))
# 'This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
print(html.unescape("I &lt;3 Python's &lt;standard library&gt;."))
# "I &hearts; Python's <standard library>."

# -----------------------------------------------------#
printDelimiter('Section 20')

# Instead of referring to a code "block", Python programmers use the word "suite." Both names are used in practice, but the Python docs prefer "suite."
if True:
    print('good')
elif False:
    print('hmm')
else:
    print('false')  # will not complain about unreachable code
print('loop exit')

# we can have nested loops
today = 'Sunday'
condition = 'Knee pain'
if today == 'Saturday':
    print('Party!')
elif today == 'Sunday':
    if condition == 'Headache':
        print('Recover, then rest.')
    else:
        print('Rest.')
else:
    print('Work, work, work.')
# -----------------------------------------------------#
printDelimiter('Section 21')

# In addition to using for to iterate over a sequence, you can be more exact and specify a number of iterations, thanks to the built-in function called range.
for i in range(3):
    print(i)
    print('hello')

for ch in "Hi!":
    print(ch)

for num in range(99, 0, -1):
    print(num)

for num in range(99, 90, -2):
    print(num)

for num in range(99, 90):  # this doesnt put any results because step is only ascending.
    print(num)

for num in range(90, 100, 3):
    print(num)

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

x = 0

while x < 4:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

else:
    print('All Done!')
# -----------------------------------------------------#
printDelimiter('Section 22')
import time

time.sleep(1)

print('slept for 1 seconds')
# -----------------------------------------------------#
printDelimiter('Section 23')

from random import shuffle #from random, import the shuffle function
mylist = [10,20,30,40,100]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))


# -----------------------------------------------------#
printDelimiter('Section XX')
print('just some text here')
"""
It can often come down to personal preference, as some programmers like to be very specific, while others don't. However, there is a
situation that occurs when two modules (we'll call them A and B) have a function of the same name, which we'll call F. If you put from A
import F and from B import F in your code, how is Python to know which F to invoke when you call F()? The only way you
can be sure is to use the nonspecific import statement (that is, put import A and import B in your code), then invoke the specific
F you want using either A.F() or B.F() as needed. Doing so negates any confusion

one way to import is to import everything like 'import F'
other way is to use 'from A import F'

once we import something in the python shell, we can ask for information about it using dir()
import random
dir(random)  --> returns all the attributes about it.
for more info, we can do help(random.randint)

CPython happens to be implemented in C. That is just an implementation detail, really. CPython compiles your Python code into bytecode 
(transparently) and interprets that bytecode in a evaluation loop.

CPython is also the first to implement new features; Python-the-language development uses CPython as the base; other implementations follow.

Jython, IronPython and PyPy are the current "other" implementations of the Python programming language; these are implemented in Java, 
C# and RPython (a subset of Python), respectively. Jython compiles your Python code to Java bytecode, so your Python code can run on the JVM. 
IronPython lets you run Python on the Microsoft CLR. And PyPy, being implemented in (a subset of) Python, lets you run Python code faster than CPython

"""
# -----------------------------------------------------#
printDelimiter('Section 25')
from turtle import *;    #any imports that the function is going to use should be defined at module level
#when used in classes in oops way, functions of python are called methods. otherwise, functions.

def draw():
    color('purple','blue')
    begin_fill()

    while True:
        forward(200)
        left(170);right(30);backward(20)
        if(abs(pos())< 1):
            break

    end_fill()
    done

#draw() #function call should be after the function is declared


# -----------------------------------------------------#
printDelimiter('Section 26')
def return_result(a,b):
    return a*b

print(return_result(10,78))

def return_result(a,b, c=20): #default value of c is 20. so it will be used if no value is passed.
    return a+b+c

print(return_result(10,78))
#print(return_result('10','78')) #error. this is also going to the function with 3 parameters
#print(return_result('10',78)) #error

print(return_result(10,78,3))
print(return_result('10','78','3')) #10783


#to reduce the confusion, we can use annotations:

def return_result(a:int,b:int) -> int:
    print('control for int')
    return a*b


def return_result(a:str,b:str) -> str:
    print('control for str')
    return a+b

print(return_result(10,78)) #well, even though I made clear, looks like python is going for the 'control for str' method for this call as well.
print(return_result('10','78'))

# above weird results are because annotations are a documentation standard, but not an enforcement mechanism. Interpreter will not pay attention to them.

#built in functions are called BIFs in python

def return_result(a,b:int=30, c:str=20): #default value of c is 20. pay attention to how annotations and default values are used for parameter c
    print('control for b?')
    return a+b+c

print(return_result(30))
print(return_result(30,40)) #where does control go? here, it sets b as 40 and takes c for its default value of 20 and returns 90
#above is because of positional assignment. Next, we can have keyword assignments also as per below example.

def return_result(a:str,b:str,c:str=30) -> str:
    print('a=',a,'b=',b,'c=',c)
    return a+b+c

print(return_result(30,40))
print(return_result(b=30,a=40))
#print(return_result(c=30,a=40)) #error  return_result() missing 1 required positional argument: 'b'
#print(return_result(b=30,a=40,30)) #error cannot have positional arguments after keyword based arguments
#print(return_result(20,b=30,a=40))#error got multiple values for argument 'a'
print(return_result(20,c=30,b=40))

# -----------------------------------------------------#
printDelimiter('Section 27')

#below are all false
print(bool(0)) #bool function returns False if expression is false or true otherwise
print(bool(0.0))
print(bool(None))
print(bool(False))
#empty strings and lists and tuples etc are also false
print(bool())
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(()))

#below are true
print(bool(1))
print(bool(0.1))
print(bool(True))
print(bool('       ')) #this is also true
# -----------------------------------------------------#
printDelimiter('Section 28')

#An empty set is represented as set(). {} is an empty dict.
l = list()
d = dict()
s = set()
t = tuple()
print(l, '--', d,'--', s, '--', t) # prints [] -- {} -- set() -- ()

