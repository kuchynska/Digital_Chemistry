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
##Update 9.10.2026
#Python Operators
print(10+5)
sum1= 100+50
sum2= 230+50
sum3=18+8
print(sum1)
print(sum2)
print(sum3)
sum4= sum2 + sum3
print(sum4)
#Arithmetic Operators
x=15
y=5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y) #Modulus, залишок від ділення 
print(x**y) #Exponentiation, піднесення до степеня
print(x//y) #Floor division, ділення з округленням вниз
#Assignment Operators
x=5
x += 3
print(x)
a=6
a -= 3
print(a)
y=7
y *= 4
print(y)
z=12
z /= 5
print(z)
#The Walrus Operator
print(x:=5)
if (x:=10)>5:
    print(x)
numbers=[1,2,3,4,5]
if (count:=len(numbers))>3:
    print(f"List has {count} numbers")
#Ternary Operator
num=6
x='Weekend'if num > 5 else 'Workday'
print(x)
num=6
x="Fri" if num==5 else "Sat"if num==6 else "Sun" if num==7 else "Weekday"
print(x)
#Comparison Operators
x=5
y=3
print(x==y)
print(x != y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print("Chaining Comparison Operators")
print(1<x<10)
print(1<x and x<10)
#Logical Operators
print("Logical Operators")
x=5
print(x>0 and x<10)
print(x<5 or x>10)
print(x<6 or x>10)
print(x<5 or x>3)
#Identity Operators
print("Identity operators")
x=["banana", "apple"]
y=["banana", "apple"]
z=x
print(x is z)
print(x is y)
print(x==y)
print(x is not y)
print("Membership Operators")
fruits={"apple", "banana", "pineapple"}
print("banana" in fruits)
print("cherry" not in fruits)
text="Hello World"
print("H" in text)
print("Hello" in text)
print("z" not in text)
print("hello" in text)
#Bitwise Operators Побітові оператори Binärsystem
#Bitwise & AND результат дорівнює 1, тільки якщо обидві цифри — 1
print(6&3) #2
#Bitwise | OR результат дорівнює 1, якщо хоча б одна цифра — 1.
print(6 | 3)
#Bitwise ^ XOR результат дорівнює 1, тільки якщо два біти різні
print(6 ^ 3)
#Bitwise NOT ~ змінює біти на протилежні: 0 стає 1, а 1 стає 0
print(~5)
#Left shift (зсув вліво)
print(5 << 1)
#Right shift (зсув вправо)
print(8 >> 1)
#Operator Precedence
print("Operator precedence")
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
print(2 ** 3 ** 2)
print(True or False and False)
#Challenge: Operators Basics
a = 15
b = 4

print(a % b)    # Залишок від ділення
print(a // b)   # Ділення з округленням униз
print(a ** b)   # Піднесення до степеня

a += 10         # Додаємо 10 до a
print(a)        # Виводимо нове значення a


#PYTHON LISTS
print("Python Lists")
# 1. Create a List - створення списку

thislist = ["apple", "banana", "cherry"]
print(thislist)


# 2. List Items - елементи списку
# Індексація починається з 0

print(thislist[0])  # apple
print(thislist[1])  # banana
print(thislist[2])  # cherry


# 3. Ordered - впорядкований список
# Елементи мають визначений порядок

fruits = ["apple", "banana", "cherry"]
print(fruits)


# 4. Changeable - список можна змінювати

fruits[0] = "orange"
print(fruits)  # ['orange', 'banana', 'cherry']


# 5. Allow Duplicates - повторення дозволені

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# 6. List Length - довжина списку
# len() рахує кількість елементів

thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # 3


# 7. List Items - Data Types
# Список може містити різні типи даних

list1 = ["apple", "banana", "cherry"]  # str
list2 = [1, 5, 7, 9, 3]             # int
list3 = [True, False, False]         # bool

print(list1)
print(list2)
print(list3)


# 8. Mixed Data Types - змішані типи даних

list4 = ["abc", 34, True, 40, "male"]
print(list4)


# 9. type() - визначення типу даних

mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # <class 'list'>


# 10. list() Constructor
# Альтернативний спосіб створення списку

thislist = list(("apple", "banana", "cherry"))
print(thislist)


# 11. Python Collections
# Чотири основні типи колекцій

my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")
my_set = {"apple", "banana", "cherry"}
my_dict = {"name": "Olha", "age": 24}

print(my_list)   # List - змінюваний, дозволяє повторення
print(my_tuple)  # Tuple - незмінюваний, дозволяє повторення
print(my_set)    # Set - не допускає повторень
print(my_dict)   # Dictionary - пари ключ: значення


#ACCESS LIST ITEMS

# 1. Access Items - доступ до елементів списку
# Індексація починається з 0

thislist = ["apple", "banana", "cherry"]

print(thislist[0])  # apple - перший елемент
print(thislist[1])  # banana - другий елемент
print(thislist[2])  # cherry - третій елемент


# 2. Negative Indexing - від'ємна індексація
# -1 означає останній елемент списку

print(thislist[-1])  # cherry
print(thislist[-2])  # banana
print(thislist[-3])  # apple


# 3. Range of Indexes - діапазон індексів
# Можна вибрати декілька елементів списку
# Кінцевий індекс не включається

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])  # cherry, orange, kiwi


# 4. Range from the Beginning - від початку списку
# [:4] означає від початку до індексу 4 (не включаючи 4)

print(thislist[:4])  # apple, banana, cherry, orange


# 5. Range to the End - до кінця списку
# [2:] означає від індексу 2 до кінця

print(thislist[2:])  # cherry, orange, kiwi, melon, mango


# 6. Range of Negative Indexes - від'ємні індекси
# [-4:-1] означає від четвертого елемента з кінця
# до останнього, але не включаючи його

print(thislist[-4:-1])  # orange, kiwi, melon


# 7. Check if Item Exists - перевірка наявності елемента
# in перевіряє, чи є елемент у списку

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# =====================================
# PYTHON - CHANGE LIST ITEMS
# =====================================

# 1. Change Item Value - зміна одного елемента
# Змінюємо другий елемент списку (індекс 1)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# 2. Change a Range of Item Values
# Зміна декількох елементів списку
# [1:3] означає індекси 1 і 2 (індекс 3 не включається)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# 3. Replace One Item with Two Items
# Замінюємо один елемент двома
# Довжина списку збільшується

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# 4. Replace Two Items with One Item
# Замінюємо два елементи одним
# Довжина списку зменшується

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# 5. Insert Items - вставлення нового елемента
# insert() додає елемент на вказану позицію
# Наявні елементи не видаляються

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# =====================================
# PYTHON - ADD LIST ITEMS
# =====================================

# 1. Append Items - додавання елемента в кінець списку
# append() додає один елемент у кінець списку

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# 2. Insert Items - вставлення елемента
# insert() додає елемент на вказану позицію
# Індексація починається з 0

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# 3. Extend List - розширення списку
# extend() додає всі елементи іншого списку

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)


# 4. Add Any Iterable - додавання інших колекцій
# extend() може додавати елементи кортежу (tuple)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)
print(thislist)


# =====================================
# PYTHON - REMOVE LIST ITEMS
# =====================================

# 1. remove() - видалення елемента за значенням
# Видаляємо "banana" зі списку

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# 2. Remove First Occurrence
# Якщо значення повторюється, remove() видаляє
# тільки перше входження

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# 3. pop() - видалення за індексом
# pop(1) видаляє другий елемент списку

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# 4. pop() - видалення останнього елемента
# Якщо індекс не вказано, видаляється останній елемент

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# 5. del - видалення елемента за індексом
# del thislist[0] видаляє перший елемент

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# 6. del - видалення всього списку
# Після del змінна thislist більше не існує

thislist = ["apple", "banana", "cherry"]
del thislist


# 7. clear() - очищення списку
# Видаляє всі елементи, але залишає порожній список

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # []


# =====================================
# PYTHON - LOOP LISTS
# =====================================

# 1. Loop Through a List - перебір елементів списку
# for проходить по кожному елементу списку
# x по черзі отримує значення кожного елемента

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)


# 2. Loop Through the Index Numbers
# Перебір списку за допомогою індексів
# len() визначає кількість елементів
# range() створює послідовність чисел 0, 1, 2

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    print(thislist[i])


# 3. Using a While Loop - цикл while
# while виконується, поки умова правильна (True)
# i = 0 означає початок із першого елемента
# i += 1 збільшує індекс на 1 після кожного повторення

thislist = ["apple", "banana", "cherry"]

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1


# 4. Looping Using List Comprehension
# Скорочений запис циклу for в одному рядку
# Виводить усі елементи списку

thislist = ["apple", "banana", "cherry"]

[print(x) for x in thislist]
