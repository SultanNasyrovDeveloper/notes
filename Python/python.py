##########
# PYTHON #
##########

# PYTHON DATA TYPES:
# ==================

# INTEGER
# -------
x = 35 # integer
x = 64.02 # float
x = int('23') # convert from the string

# STRING
# -------
#  indexing
# when indexing starting index substring is always
# included to the result but nir the end index value
word = 'something'
string = word[2] # get substring with index 2: 'm'
string = word[1:3] # get substring from element with index 1 to element with index 3: 'ome'
string = word[:3] # get substring from start to element with index 3: 'som'
string = word[4:] # get substring from element with index 4 to the end: 'able'
string = word[::2] # get substring that contains every second element: 'smtig'
string = word[::-1] # getreverse string: 'gnihtemos'
# formatting
string = 'Hello, {}!'.format('Vasya') # 'Hello, Vasya!'
string = '{0}, {1}, {2}'.format('a', 'b', 'c') # 'a, b, c'
string = '{}, {}, {}'.format(word, 'b', 'c') # 'a, b, c'
string = '{0.id}, {0.name}, {0.description}'.format(obj) # object can be passed here
string = f'{variable_name}'  # new in python 3.6
# string methods
string = 'some string'
string.capitalize() # Some string
string.count('i') # 1
string.find(str, beg=0, end=len(str))
string.isdigit() # false
string.lower() # some string
string.upper() # SOME STRING
string.replace('s', 'z', 1) # zome string
string.split() # ['some', 'string']
string.strip() # 'some string'

# LIST
# -----
some_list = list(iterable)
some_list = [1, 2, 3, 4, 5]

# some useful examples
for x in sorted(some_list): pass # sorted dlist
for x in set(some_list): pass # unique
for x in reversed(some_list): pass # itteration in reversed list

#  methods
list =  [ 23, ]
list.clear() # []
list.append('any element')   # [ 'any element']
list.extend([1, 2, 3])   # [ 'any element', 1, 2, 3]
list.copy() # [ 'any element']
list.deepcopy() # creates new list object
list.count('any element')  # 1
list.extend(new_list) # Add the elements of a list (or any iterable), to the end of the current list
list.index() # position of element
list.insert(0, 'new element') # ['new element', 'any element']
list.pop(0) #
list.remove('any element') # []
list.sort(reverse=True)

#  list comprehensions
[output_expression for x in some_list if optional filter]
# examples
input_list = [1, 2, 3, 4, 5, 6]
output_list = [x + 1 for x in input_list if x >= 2]


# SET
# ----
# Collection of unsorted, unindexed, unique values
some_set = set(some_list)
some_set = {1, 'string', 334}
some_set.add('new string')
some_set.remove('new string')
x = len(some_set)

Examples:
a = [ i*i for i in range(1,10)] # [1, 4, 9, 16, 25, 36, 49, 64, 81]
a = [ i*i for i in range(1,10) if i % 2 == 0] # [4, 16, 36, 64]


# DICTIONARY
# ------------

key - integer, string or tuple(unique value)

my_dict = {'some_string': 'value'}
my_dict[1] = 123 # {'some_string': 'value', 1: 123}

x = my_dict['some_string'] # x = 123
del(my_dict['some_string'])
del dict['Name']
x = len(my_dict) # number of pairs

- methods
my_dict.clear() # my_dict = {}
x = my_dict.has_key('some_key') # False
x = my_dict.get('some_key')
x = my_dict.pop('some_key')
x = my_dict.copy() # псевдокопия
x = my_dict.deepcopy() # true copy
x = my_dict.items() # to itterate through key and values
x = my_dict.keys()
x = my_dict.values()
x = my_dict.update(m) # another dict in the end

Examples:


# OPERATORS
# ==========

Arithmetic
-----------
x = 3 + 2   # 5
x = 3 - 2   # 1
x = 3 * 2   # 6
x = 2 ** 3  # 8
x = 10 / 2  # 5
x = 9 % 4   # 1
x = 12 // 5 # 2

- Comparison
-------------
2 == 2   # true - проеряет равенство значений двух разных объектов
2 != 2   # false - обратное
4 > 2    # true
4 < 2    # false
5 >= 5   # true
6 <= 3   # false

- Logical
----------
2 and 2
5 or 3
not 54

- Membership
--------------
some_list = []
if x in some_list:
    pass
elif x not in some_list:
    pass

x is m # проряет указывают ли на один и тот же объект
x is not m # обратное


LOOPS
------

- While
---------
while x > 15:
    print(x)
    x += 1

- For
for smth in some_list:
    print(smth + ' some string')

# -= continue =-
# Оператор continue начинает следующий проход цикла,
#   минуя оставшееся тело цикла (for или while)

# -= break =-
# Оператор break досрочно прерывает цикл
for letter in 'some string':
    if letter == 'i':
        break
    print(letter * 3, end='')

# -= else =-
# Блок инструкций внутри else выполнится только в том случае,
#   если выход из цикла произошел без помощи break.
for letter in 'some string':
    if letter == 'a':
        print('В строке найдена буква "а"')
        break
else:
    print('Буквы в строке нет')

# === Examples:

fruits = ['banana', 'apple',  'mango']

for index in range(len(fruits)):
   print('Current fruit :', fruits[index])

#
# xxxxxxxxxxxxxxxxxxxxxxxx FUNCTIONS xxxxxxxxxxxxxxxxxxxxxxxx

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

default_par = x

def adding(parametr1, parametr2=default_par):
    x = parametr1 + parametr2
    return x

def unknown(*args):
    for argument in args:
        print(argument)

m = adding(5, 6) # m = 11

# === built-in functions ===

type()
str()  # is used to make string or create output for end user
repr()  # is used to make representation needed for developers
range(start, stop, step)  # return list of numbers
any()
bound()
groupby()
ord()
sorted() # sorts object
reversed()  # object in reverse oreder

# === functional programming ===
# map(func=function, sequence)  применяет функцию к кажому элементу последовательности
# возвращает последовательность такое же длины
# filter(func=function, sequence) применяет функцию к каждому элементу
# возвращает те элементы исходного списка для которых функция вернула True

# -= Recursion =-
# Рекурсией в программировании называется ситуация, в которой функция вызывает саму себя.

def fact(num):
    if num == 0:
        return 1 # По договоренности факториал нуля равен единице
    else:
        return num * fact(num - 1)

# -= Lambda =-
# lambda arguments: expression

# В качестве arguments передается список аргументов, разделенных запятой,
# после чего над переданными аргументами выполняется expression

multiply = lambda x,y: x * y
multiply(3, 8)

# === Examples:


# python built-in methods


# xxxxxxxxxxxxxxxxxxxxxxxx EXCEPTIONS xxxxxxxxxxxxxxxxxxxxxxxx

try:
    # try to execute this code block
except TypeError:
    # if Type error occurs do this block of code
except ArithmeticError:
    # if arithmetic errror occurs do this block of code
else:
    # in all of other situations do this
finally:
    # and no matther what do this


# xxxxxxxxxxxxxxxxxxxxxxxx TYPING xxxxxxxxxxxxxxxxxxxxxxxx




# xxxxxxxxxxxxxxxxxxxxxxxx OOP xxxxxxxxxxxxxxxxxxxxxxxx
class SomeClass:
    variable = 'smth'  # class variable -  data that same for all instances

    def __init__(self):
        self.var = 'smth'  # instance var - unique for any instance

    def foo(self):
        print(SomeClass.variable)  # or self.variable

x = SomeClass()
x.variable = 'new'
SomeClass.variable = 'new'

# ===== princips =====
# -= Полиморфизм =-
# В разных объектах одна и та же операция выполняет разные функции

example = 1 + 2  # 3
example = 'a' + 'b'  # 'ab'

# Инкапсуляция
#

# Наследование
# Можно создавать классы на основе имеющихся классов

class A:
    a = 'some attr'

class B(A):
    pass

b = B()
print(b.a)  # some attr

# Композиция
# Объект может включать в себя другие объекты


# ===== methods =====

# -= classmethod =-
# automatically takes class as a first arguement instead of instance
@classmethod
def some_class_method(cls):
    print(cls.variable)

@classmethod
def alternative_constructor(cls, name, last_name):
    name = name + '1'
    last_name = last_name + '2'
    return cls(name, last_name)

# -= staticmethod =-
# don't take class or self as a first arguement
# method is static if it dont access class ao instance vars inside the function

@staticmethod
def static_method(smth):
    pass

# -= property =-
# property decorator allows to access function result as as instance attrubute
# we can acces it but we can't change it
@property
def full_name(self):
    return name + last_name

# in order to set property values and other variable this method depends on
@full_name.setter
def full_name(self, name):
    self.name = name

# deleter used to make some clean up work when ypu delete property
@full_name.deleter
def full_name(self):
    pass


# === Examples:
