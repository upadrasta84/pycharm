#installed mysql connector using pip as pip install mysql-connector
#before this, I used db4free.net to create database and use a chrome extension called mysql console to create test table on mysql
#https://chrome.google.com/webstore/detail/mysql-console/cakepohgdbjbenkcpkkacmohgfjhnjoh/related?hl=en

import mysql.connector

dbconfig = { 'host': 'db4free.net',
 'user': 'karr123',
 'password': 'Ba9TM*u26NkWz9z',
 'database': 'karsql', }

conn = mysql.connector.connect(**dbconfig) #here the strange syntax of ** means that the entire dict object is passed and python will expand it to 4 different arguments as needed

print(conn)

#To send SQL commands to your database (via the just-opened connection) as well as receive results from your
#database, you need a cursor. Think of a cursor as the database equivalent of the file handle for files

cursor = conn.cursor()
cursor.execute('show tables')

#When you type the above cursor.execute command at the >>> prompt, the SQL query is sent to your
#MySQL server, which proceeds to execute the query (assuming it’s valid and correct SQL). However, any
#results from the query don’t appear immediately; you have to ask for them.
#You can ask for results using one of three cursor methods:
#• cursor.fetchone retrieves a single row of results.
#• cursor.fetchmany retrieves the number of rows you specify.
#• cursor.fetchall retrieves all the rows that make up the results.


res = cursor.fetchall()
print(res)

cursor.execute('select * from test')
res = cursor.fetchall()
for row in res:
 print(row) #here we have only 1 column, but we can use row[0], row[1] etc to pick values from first column, second column and so on

cursor.execute('delete from test')

for val in ['1','2','3','4','5','6','7','8','9','10'] :
 cursor.execute('insert into test values('+val+')')

conn.commit()

_SQL = """insert into test(abc) values(%s)"""
for val in ['11','12','13','14','15','16','17','18','19','20'] :
 cursor.execute(_SQL, (val,)) #insert with sql query and tuples. note that it must be a tuple. first i tried with just (val).
 # note that a single value inside paranthesis must end with a comma to be considered as a tuple. code was erroring and i wasnt able to figure out why until i did understand this

conn.commit()

cursor.close()
conn.close()

#we can do above like this:
#however to use the below, we need a context manager
#The context management protocol lets your write a class that hooks into the “with” statement.

#classes with context. the context management protocol dictates that any class you create must define at least two magic
#methods: __enter__ and __exit__. We can also have __init__ method for initialization. When you adhere to the
#protocol, your class can hook into the with statement.The protocol further states that dunder enter can (but doesn’t have to) return a value
#to the with statement .As the code in the with statement’s suite may fail (and raise an exception), dunder
#exit has to be ready to handle this if it happens.

#Decorators are specifically concerned with augmenting existing functions with additional functionality,
#whereas context mangers are more interested in ensuring your code executes within a specific context, arranging for code to run before a
#with statement as well as ensuring that code always executes after a with statement.

from MyDBConnMgr import UseDatabase #since we have import mysql.connector in MyDBConnMgr, we dont need to import it again here

with UseDatabase(dbconfig) as cursor:  #this will automatically close the conn and cursor
  _SQL = """insert into test(abc) values(%s)"""
  cursor.execute(_SQL, ('21',))

