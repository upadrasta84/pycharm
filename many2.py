# -----------------------------------------------------#
# printDelimiter('Section 29') we cannot use without importing the module first.
# -----------------------------------------------------#
import sys

from main import printDelimiter
# above works because main is in the same folder as many2. modules are checked in:
# 1. your current work directory
# 2. your implementer's site-package locations
# 3. the standard library locations

# initially, I had printDelimiter in main.py. when I imported it as per above and ran many2.py (not many.py), all code from many.py was also executing
# then i got confused as I expected it to run code only from #many2.py... later learnt that, any code at indentation level 0 is run by default.
# so i moved the function printDelimiter to main.py and imported the 'main' module to both many.py and many2.py. however i was also surprised why main.py code didnt run
# this is because it has code at indentation level 1 with the construct 'if __name__ == '__main__':',
# whatever file we run using 'python sample.py', python assigns the hidden and default variable of __name__ to __main__.
# #so we usually check to see this is our correct entry point file

print(__name__)  # will print __main__ if this is the program we are running using 'python many2.py'
printDelimiter('Section 30')


# tuple unpacking
def fun_ret_tuple():
    return (1, 2)


a = fun_ret_tuple()
b, c = fun_ret_tuple()
print(a)
print(b)
print(c)


def fun_ret_tuple():
    return (1, 2, 3)


a = fun_ret_tuple()
b, c, d = fun_ret_tuple()
print(a)
print(b)
print(c)

print(d)

# typically, we have all our functions at top and followed by the name==main construct to create the entry point for the entire application and run application from there
# -----------------------------------------------------#
# to run a function for multiple items, we can use map
# to filter items based on a common function, we can use filter
printDelimiter('Section 31')


def is_even(num):
    return num % 2 == 0


print(list(
    map(is_even, [2, 4, 5, 6, 7, 8])))  # we first apply map, then convert the returned items to a list and print it
print(list(filter(is_even, [2, 4, 5, 6, 7, 8])))  # returns and prints only even numbers.. cool


# the above function can also be written in a single line like this:
def is_even(num): return num % 2 == 0


# lambdas basically help us save space by writing above as below:

even = lambda num: num % 2 == 0
# we can then do:
print(list(map(even, [2, 4, 5, 6, 7, 8])))

# to make it even more consice, we can do:
print(list(map(lambda num: num % 2 == 0, [2, 4, 5, 6, 7, 8])))
print(list(filter(lambda num: num % 2 == 0, [2, 4, 5, 6, 7, 8])))  # coolest!

# -----------------------------------------------------#
printDelimiter('Section 32')
"""
Python uses LEGB rule for figuring out which variable to use:
L - Local - within function or Lambda
E - Enclosing - enclosing function's locals. 
G - Global - within the module
B - Built-in (Python) - ex: open, range, SyntaxError etc
"""

# In python, we can have function within function:

name = 'Global'


def print_name():
    name = 'Enclosing'

    def print_name_local():
        name = 'Local'
        print(name)  # Local

    print_name_local()
    print(name)  # Enclosing, for this function, it is local


print_name()
print(name)  # Global

# -----------------------------------------------------#
printDelimiter('Section 33')
"""
PyPi is a repository of all the 3rd party Python packages
similar to RubyGems (Ruby)/Packagist (PHP)/NPM (Node.js)/CPAN (Perl)
we can use 'pip install' to install these packages. pip comes with Python/Anaconda distribution
"""

# C:\Users\Karthik>pip install colorama
# Defaulting to user installation because normal site-packages is not writeable
# Collecting colorama
# Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
# Installing collected packages: colorama
# Successfully installed colorama-0.4.4


from colorama import init
from colorama import Fore

init()
print(Fore.RED + "Some Red Text")
print(Fore.GREEN + "Some Red Text")
print(Fore.LIGHTWHITE_EX + "Some Normal Text")

# to change interpreter in pycharm, i did file > settings > project settings and from there, selected system interpreter.
# system interpreter was pointing to anaconda as i set anaconda in PATH during installation. so had to change that first.

# -----------------------------------------------------#
printDelimiter('Section 34')

# to create our own modules, we can have directories and use them as packages and subpackages as in java
# for that, we need many2.py files.

# created mainpackage and subpackage and created a couple of simple modules in each. we use them like below:

from mainpackage import mainmodule
from mainpackage.subpackage import submodule

print(mainmodule.square(3))
print(submodule.squaresub(4))

# above worked fine even without many2.py files. but i created them later

# -----------------------------------------------------#
printDelimiter('Section 35')
"""
If you used a library, package, or framework that doesn't come with the Python standard library (think anything you needed to install with pip or conda), 
Python needs to know about that, so the program knows where to look when it finds commands that it doesn't recognize.
You store a list of those packages in requirements.txt or a Pipfile. These are the dependencies of your code and are necessary for a successful build.

Flake8 is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder's McCabe script. It is a great toolkit for checking your code base against coding 
style (PEP8), programming errors (like "library imported but unused" and "Undefined name") and to check cyclomatic complexity.

The purpose of pyflakes is to statically analyze your code to make sure there will be no name errors or unused variables/imports.

pylint, pep8, and flask8 are the lint tools for python - at citi, we seem to be using pylint - static code analysis tools

look at test dir. python has standard unittest module for unit testing. these are run using the command:
python -m unittest

Python Package Index - PyPI --> used to package our modules and distrubute them


"""

"""
installed flake8, pytest etc using:
pip install flake8 pytest pytest-cov

to create requirements.txt, use: pip freeze requirements.txt  .. now requirements.txt contents are:
atomicwrites==1.4.0
attrs==21.2.0
colorama==0.4.4
coverage==6.2
flake8==4.0.1
iniconfig==1.1.1
mccabe==0.6.1
packaging==21.3
pluggy==1.0.0
py==1.11.0
pycodestyle==2.8.0
pyflakes==2.4.0
pyparsing==3.0.6
pytest==6.2.5
pytest-cov==3.0.0
toml==0.10.2
tomli==2.0.0

in docker, we can use:
pip install -r requirements.txt
pip is package installer for Python (pip)

in citi, we are using flask framework.


to create our own distribution, have 2 files: README.txt and setup.py. Readme can be empty.
then use: py -3 setup.py sdist
running above will create the package in dist folder
to install, use D:\Karthik\workspaces\pycharm>pip install dist/many2-1.0.tar.gz

Flask provides a collection of modules that help you build server-side web
applications. It’s technically a micro web framework, in that it provides the
minimum set of technologies needed for this task. This means Flask is not as
feature-full as some of its competitors—such as Django, the mother of all
Python web frameworks—but it is small, lightweight, and easy to use.


"""

# -----------------------------------------------------#
printDelimiter('Section 36')

#Depending on the situation, Python’s function argument semantics support both call-by-value and call-by-reference.
#What actually happens is that the interpreter looks at the type of the value referred to by the object reference (the memory address) and, if the variable refers to a
#mutable value, call-by-reference semantics apply. If the type of the data referred to is immutable, call-byvalue semantics kick in
def double(arg):
 print('Before: ', arg)
 arg = arg * 2
 print('After: ', arg)

def change(arg):
 print('Before: ', arg)
 arg.append('More data')
 print('After: ', arg)

arg = 20
print(double(arg))
print('after function',arg) #pass by val

arg=['2']
print(change(arg))
print('after function',arg) #pass by ref



# -----------------------------------------------------#
printDelimiter('Section 37')
"""
A virtual environment lets you create a new, clean Python environment
within which you can run your code. You can install third-party modules into
one virtual environment without impacting another, and you can have as many
virtual environments as you like on your computer, switching between them by
activating the one you want to work on. As each virtual environment can maintain
its own copy of whatever third-party modules you wish to install, you can use two
different virtual environments, one for each of your client projects discussed above.

we can use the virtual environment
technology, called venv, that ships with Python 3’s standard library, or install the
virtualenv module from PyPI
"""

# -----------------------------------------------------#
printDelimiter('Section 38')
#all built-in exceptions inherit from the Exception class.
#One such function is exc_info, which provides information on the exception
#currently being handled. When invoked, exc_info returns a three-valued
#tuple where the first value indicates the exception’s type, the second details the
#exception’s value, and the third contains a traceback object that provides
#access to the traceback message (should you need it). When there is no currently
##available exception, exc_info returns the Python null value for each of the
#tuple values, which looks like this:(None, None, None).

try:
    print(2+'2')
except TypeError:
    print('except TE')
    err = sys.exc_info()
    for e in err:
        print(e)
except:
    print('except')
else:
    print('optional else')
finally:
    print('finally')

try:
    print(2+2)
except TypeError:
    print('except TE')
except:
    print('except')
else:
    print('optional else')
finally:
    print('finally')


try:
    can_have_whatever_here_which_is_lame()
except Exception as err: #assign the exception to err variable
    print('of course you can')
    print(err)
    print(str(err))

try:
    print('you can raise your own exception')
    raise Exception('your own custom exception')
except:
    err = sys.exc_info()
    for e in err:
        print(e)

class KarCustomException(Exception):
    pass

try:
    print('you can raise your own CUSTOM exception')
    raise KarCustomException('your own custom exception')
except KarCustomException as err2:
    err = sys.exc_info()
    for e in err:
        print(e)
    print('KarCustomException: ', err2)


# -----------------------------------------------------#
printDelimiter('Section 39')

def hello(hi_bye):
    print('hello fkr')

    def welcome():
        print('welcome')

    def bye():
        print('bye')

    if hi_bye == 'hi':
        return welcome
    else:
        return bye


hello('hi')
greet = hello #we are passing a reference
del hello
try:
    print('trying to call hello after deleting it')
    hello('hi')
except:
    print('if hello doesnt work, greet should')
    greet('bye')

mybye = greet('bye') #we can only use greet at this stage as reference to hello is deleted.

#mybye now has a reference to the 'bye' function within the hello function. we can call mybye as a function like so:
mybye()

#the idea here is to introduce to decorators. the idea behind is that we can use functions as variables and pass that reference around.

def new_fun_with_fun_param(my_fun_ref):
    print(my_fun_ref)

new_fun_with_fun_param(mybye)
new_fun_with_fun_param(mybye())

# -----------------------------------------------------#
printDelimiter('Section 40')
#with the above decorator context, here is some code. we are going to try to extend a function with additional functionality by adding a decorator

def simple_print():
    print('hello world')

def advanced_print(simple_print_fun):

    def wrapper_simple_print():
        print('before hello')
        simple_print_fun()
        print('after hello')

    return wrapper_simple_print

@advanced_print
def decorated_print():
    print('hello world')

decorator = advanced_print(simple_print)
decorator()   #essentially advanced_print(simple_print)() and decorated_print() are both the same!!

decorated_print()

# -----------------------------------------------------#
printDelimiter('Section 41')

def my_fun(*args):
    print(sum(args))

my_fun(1)  #with my_fun having *args, we can pass multiple parameters. *args is a tuple here
my_fun(1,2,3)
#my_fun(1,4,7,9,'s') #error

def my_fun(*args2): #the name can be anything. it should start with *
    print(*args2)
    for x in args2:
        print(x)

my_fun(1,4,7,9,'s')

#while *args is a tuple, **kwargs (keyword args) is a dict
def my_fun(**something): #name can be anything. should be **something
    print(something)

my_fun(arg='blah')

def my_fun(*args, **kwargs):
    print(args, kwargs)

my_fun(1,2,'3',arg='blah', wag='tail')

# my_fun(1,2,'3',arg='blah', wag='tail', '4') #this is not ok as python will not know what to do with 4. positional argument cannot follow keyword argument

#def my_fun(**kwargs, *marg): T**arg should be the last parameter. error



#decorators with parameters
def simple_print(str):
    print('hello ', str)

def advanced_print(simple_print_fun):

    def wrapper_simple_print(*args, **kwargs): #to pass parameters to the method we are decorating, use *args and **kwargs.
        print('before hello')
        return simple_print_fun(*args, **kwargs) #and then pass the *args and **kwargs to the original function.. we need return statement here to capture return value of the function being decorated
        print('after hello')

    return wrapper_simple_print


@advanced_print
def decorated_print(str):
    print('hello ', str)
    return 'tst'

decorator = advanced_print(simple_print)
decorator('world')

decorated_print('world')

ret_val = decorated_print('world')
print('print ret_val to see if decorated methods can return ', ret_val)
# -----------------------------------------------------#
printDelimiter('Section 42')

#generator functions allow us to write a function that can send back a value and then later resume to pick up where it left
#they will automatically suspend and resume their execution and state round the last point of value generation

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_cubes(10):
    print(x)

#with generators, we dont have to store the results in 'result' variable and then return it, instead, we can yield a variable value and function keeps track of it with step size of 1

def gen_fibon(n):
    a, b = 1, 1
    for x in range(n):
        yield a #Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when
                # the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed a generator.
        a, b= b, a+b  # a = b , b = a+b

for x in gen_fibon(10):
    print(x)

x = gen_fibon(10)
for i in range(9): #iterating till only 9 ... one more yield left
    print(next(x)) #next will call the function while keeping track of its current state.

print(next(x)) #no problem.. this is the last yield
# print(next(x)) # we will get error of StopIteration if we do it again

try:
    print(next(x))
except StopIteration:
    print('all yields done')


#look around line 250 in many.py. it talks about comprehensions.
#below may look like that but it is a generator. in list comp, we have square brackets but in below we have parenthesis
for i in (x*3 for x in [1, 2, 3, 4, 5]):
 print(i)


"""
when you replace a listcomp’s surrounding square brackets with parentheses, the results are the same; that is, the generator and
the listcomp produce the same data. However, they do not execute in the same way. If you’re scratching your head at the previous sentence, consider this: when a listcomp
executes, it produces all of its data prior to any other processing occurring. Taken in the context of the example at the top of this page, the for loop doesn’t start
processing any of the data produced by the listcomp until the listcomp is done. This means that a listcomp that takes a long time to produce data delays any other code
from running until the listcomp concludes.

Below shows difference between listccomp and generator. listcomp will fetch all results at once unlike generator
"""

import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
for resp in (requests.get(url) for url in urls):
 print(len(resp.content), '->', resp.status_code, '->', resp.url)


urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
for resp in [requests.get(url) for url in urls]: #note only square brackets and parenthesis lines are changing
 print(len(resp.content), '->', resp.status_code, '->', resp.url)


# -----------------------------------------------------#
printDelimiter('Section 43')

for letter in 'hello':
    print(letter)

try:
    next('hello') #not ok as a string is not an iter. we need to get an iter on it before calling next function on it
except TypeError:
    string_iter = iter('hello')
    print(next(string_iter))
    print(next(string_iter))

# -----------------------------------------------------#
printDelimiter('Section 44')
import requests
result = requests.get('http://www.example.com')
print(result)
print(result.text)

import bs4

soup=bs4.BeautifulSoup(result.text,'lxml')
print(soup)

# -----------------------------------------------------#
printDelimiter('Section 45')

print(soup.select('title'))
print(soup.select('title')[0].getText())

print(soup.select('title')) #all elements with title tag
print(soup.select('#some_id')) #all elements with id as some_id
print(soup.select('.some_class'))#all elements with class as some_class
print(soup.select('div span'))#all elements named span within a div element
print(soup.select('div > span'))#all elements named span directly within a div element


# -----------------------------------------------------#
printDelimiter('Section 46')

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')
image_info = soup.select('.thumbimage')
computer = image_info[0]
print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
f = open('my_new_file_name.jpg','wb')
f.write(image_link.content)
f.close()

# -----------------------------------------------------#
printDelimiter('Section 47')
def fun(var1, var2):
    print('python threads!', var1, var2)

from threading import Thread
t = Thread(target=fun, args=('var1',3))
t.start();


# -----------------------------------------------------#
printDelimiter('Section 48')

import os
os.chdir(".")

with open('test.csv') as raw_data:
    print(raw_data.read())

import csv

with open('test.csv') as data:
    for line in csv.reader(data):
        print(line)


import pprint #pretty print
with open('test.csv') as data:
    for line in csv.DictReader(data):
        pprint.pprint(line)

#some useful stuff from os package:
print(os.listdir())
print(os.listdir("C:\\Users"))

#You can use the built-in **shutil** module to to move files to different locations.
import shutil
"""
os.unlink(path) which deletes a file at the path your provide
os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.
"""


# -----------------------------------------------------#
printDelimiter('Section 49')

from collections import Counter
lst = [1, '1', 2, 2, 3, '1', 3, 1]
str = "hi how are you how is kart how is bert"

print(Counter(lst))
print(Counter(str.split()))
c=Counter(str.split())
print(c.most_common())

""" most common python modules
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts

from advanced collections, we can also have defaultdict so that asking for any key will return a value but not an error
then we can also have namedtuples and many more 
"""

