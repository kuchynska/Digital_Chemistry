print ("Hello, World")
print ("I am Olha and i am learning Python")
print ("The Python version is:")
import sys
print(sys.version)
#Python Indentation
if 5 > 3:
    print("Five is greater than three!")
    print("That's true!")
#Variables
x=5
y="Hello"
print(x)
print(y)

"""
this is a comment
written in
more than just one line
"""
#data type of a variable
print("Data types of variables")

myvar=5
a=5,2
b="baby"
c=3.14

print("Ganzzahl")
print(type(myvar)) #int=integer(Ganzzahl)

print("Sammlung von Werten")
print(type(a)) #tuple=Tupel

print("Wort")
print(type(b)) #str=string(Text)

print("Gleitkommazahl")
print(type(c)) #float=Gleitkommazahl

#Semikolon
print("Physics");print("Chemistry");print("Biology")

#Challenge: Statements
print("Hello World")
print("Have a good day!")
print("Learning Python is fun!")

print("Print without a new line")
#Print Without a New Line
print("Hello", end=" ")
print("World")

print("Print numbers")
#Print Numbers 
print(8)
print(30)
print(2002)
print("23") #string=text
print(3+3) #addition
print(2*4) #multiplication
print(10/2) #division
print(10%3) #modulus=остача від ділення

#Mix Text and Numbers
print("I am",24,"years old")
print("Temperature:", 15,"°C")
temperature=20
print("Temperature:",temperature, "°C")
age=30
print("Age:",age,"years old")
#Challenge: Output / Print
print("I am",25)

#Creating a comment
#print("Hello World") #it can also be used to prevent Python from executing code
print("Hello mate")
#This is a comment
#written in more
#than just one line

""""
This ia also a comment
written in more than just one line
"""
#Challenge: Comments

#This is a comment
#print("This should not run")
"""
This is
a multiline
comment
"""
#Variables

x=5
y="John"
print(x)
print(y)

a=5
print(type(a))
a="Anna"
print(type(a))

#Casting =перетворення типів даних
x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))  

#Single or Double Quotes
b="Hello"
#is the same as
b='Hello'

#Case-Sensitive
a=4
A='Sally'
#A will not overwrite a

#Variable Names
myvar='John' 
my_var='John'
_my_var='John'
myVar='John'
MYVAR='John'
myvar2='John'

#Multi Words Variable Names
myVariableName="John" #camel case
MyVariableName="John" #pascal case
my_variable_name="John" #snake case

#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Unpack a Collection
fruits=["mango","pineapple","kiwi"]
x,y,z=fruits
print(x)
print(y)
print(z)
print(x,y,z)

#Output Variables
x='Python'
y='is' 
z='awesome'
print(x,y,z)
print(x + " " + y + " " + z)
x=5
y=10
print(x+y)
m=5
n='John'
print(m,n)

name='Olha'
age=24
print(name,age)

#Global Variables
x='awesome' 
def myfunc():
    x='fantastic'
    print('Python is ' + x, end=' ')
myfunc()
print('and ' + x)

x='awesome'
def myfunc ():
    global x
    x='fantastic'
myfunc()
print('Python is ' + x)

#Data Types
x=1j
print(type(x)) #complex number
x=['apple','banana','cherry']
print(type(x)) #list
x=('apple','banana','cherry')
print(type(x)) #tuple
x=range(6)
print(type(x)) #range
x={'name':'John','age':36}
print(type(x)) #dict
x={'apple','banana','cherry'}
print(type(x)) #set

#Python Numbers
x=1
y=2.8
z=3+5j
print(type(x)) #int
print(type(y)) #float
print(type(z)) #complex
a=float(x)
b=complex(y)
c=int(y)
print(a)
print(b)
print(c)    
#random
import random
print(random.randrange(1,10))

#Specify a Variable Type
print('Specify a Variable Type')
x=int(1)
y=int(2.8)
z=int("3")
print(x)
print(y)
print(z)
x=float(1)
y=float(2.8)
z=float("3")
print(x)
print(y)
print(z)
x=str('z2')
y=str(2.8)
z=str(3)
print(x)
print(y)
print(z)

#Strings
print('He is called "Johny"')
a='John'
print(a) 
b='''Hello 
all people '''
print(b)
#Strings are Arrays
a='Hello'
print(a[1]) #prints e
print(a[0]) #prints H
#Looping Through a String
for x in 'banana':
    print(x)
#String Length
a='Millionaire'
print(len(a))
b='It`s free to think like a millionaire'
print(len(b))
#Check String
txt='It`s free to think like a millionaire'
print('free' in txt) 
txt= 'We are the champions my friend'
if 'friend' in txt:
    print('Yes, "friend" is present')
if 'free' not in txt:
    print('No, "free" is not present')

#Slicing Strings
b='Hello, World!'
print(b[2:5])
print(b[:5])
print(b[2:])
#Negative Indexing
print(b[-7:-1])
#Modify Strings
a='I`m tired'
print(a.upper())
print(a.lower())
b='   Hello, World!    '
print(b.strip())
print(b.replace("H","J"))
txt="Me and my friend study chemistry"
print(txt.replace("chemistry","biology").upper())
print(txt.split(" "))
#String Concatenation
a="Hello,"
b="New Day"
print(a + " " + b)
c=65
d=5
e=(c+d)
print(e)
#f-string
age=36
txt=f"My name is John, I am {age}"
print(txt)
price=67.986
txt=f"The price of this kettle is {price:.2f} $"
print(txt)
txt=f"The price is {20*59}$"
print(txt)

#Escape Character
txt="We are the so-called \"Vikings\" from the north"
print(txt)
print("Hello\nWorld")
print("Hello\tWorld")

#String Methods
print("hello world".capitalize())
print("HELLO".lower())
print("hello".upper())
print("hello world".title())
print("Hello".swapcase())
print("Hello World".find("World"))
print("banana".count("a"))
print("Hello".startswith("He"))
print("Hello".endswith("lo"))
print("I study chemistry".replace("chemistry","biology"))
print("cherry,blueberry,raspberry".split(","))
print("-".join(["a","b","c"]))
print("    Hello   ".strip())
print("    Hello   ".lstrip())
print("    Hello   ".rstrip())
print("Hello".isalpha())
print("123".isdigit())
print("abc123".isalnum())
#Challenge: Strings Basics
txt="Hello, World!"
print(txt[2:5])
print(txt.upper())
name="Python"
print(f"I love {name}")
#Update 6.10.2026
#Python Booleans True or false

print(10<9) #false
print(56>43) #true
print(10==9) #false
#with "if"
a=200
b=57
if a>b:
    print("a is greater than b")
else: 
    print ("a is not greater than b")
c=33
d=330
if c>d:
    print("c is greater than d")
else:
    print("c is not greater than d")

print("True-values")   #True
print(bool("Hello"))
print(bool(19))
print(bool(123))
print(bool("abc"))
print(bool(["apple","banana","cherry"]))

print("False-values") #False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def add():
    return 2+3
x=add()
print(x)

def is_positive(x):
    return x>0
print(is_positive(5))

def myfunc():
    return True
if myfunc():
    print("YES!")
else:
    print("NO!")
#isinstance()
x=200
print(isinstance(x,int))
y=20.5
print(isinstance(y,float))
z="banana"
print(isinstance(z,str))

#Challenge: Booleans
print("Challenge: Booleans ")
print(10>9)
print(10==9)
print(bool("Hello"))
print(bool(0))