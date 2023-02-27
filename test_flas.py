#not running from pycharm.. run using python test_flas.py from command prompt
#install flask using pip install flask. dont create file as flask.py.. use any other names

from flask import Flask, render_template, redirect #see how we are importing 2 things
from flask import request

app = Flask(__name__) #the double __ name and conventions are reffered to as dunder names in py world and collectively called 'the dunders'
#As well as the dunders, there is also a convention to use a single underscore character to prefix certain variable names.
# Some Python programmers refer to single-underscore-prefixed names by the groaninducing name "wonder" (shorthand for "one underscore").

#the __name__ == __main__ is referred to in Python as dunder name dunder main


# use http://127.0.0.1:5000/
@app.route('/hello2')  #lines which start with @ are called decorators and borrowed from the Java world
#Decorators let you change the behavior of an existing function without having to change the function's code
def hello() -> str:
 return 'Hello world from Flask! your ip is '+request.remote_addr

#this uses flask's redirect to redirect root page to entry
@app.route('/')
@app.route('/home') #we can have multiple paths mapped to same function also
def hello3() -> '302':
 return redirect('/fk')

# use http://127.0.0.1:5000/fk?username=kar
@app.route('/fk')
def hello2() -> str:
 username = request.args.get('username')
 if username == None:
  return 'blah2'
 else:
  return 'Hello world from Flask!'+username


#Flask comes with a built-in object called request that provides easy access to posted data. The request object contains a dictionary attribute called
#form that provides access to a HTML form's data posted from the browser.
@app.route('/testjinja', methods=['POST']) #without specifying method, i was getting an error saying method not allowed.
def do_search() -> str:
 phrase = request.form['phrase'] #the request dict also has few other keys such as request.remote_addr, request.user_agent etc
 letters = request.form['letters']
 print(phrase,letters)
 return str('fkr')

#The template engine shipped with Flask is called Jinja2, and it is both easy to use and powerful. Look at test_jinja.html
@app.route('/entry')
def entry_page() -> 'html':
 return render_template('entry.html', #entry.html etc files will be in templates folder
 the_title='Welcome to search4letters on the web!')

#any changes here will be automatically loaded by flask without restarts.
app.run(debug=True) #debug=True will auto-reload without having to restart the console.