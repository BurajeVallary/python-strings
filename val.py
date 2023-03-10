>>> s="AkiraChix"
>>> s.index("a")
4
>>> s[0]
'A'
>>> s[3]
'r'
>>> s[6]
'h'
>>> s[8]
'x'
>>> s[9]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-8]
'k'
>>> s[9]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-9]
'A'
>>> s[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-19]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-1]
'x'
>>> s[-5]
'a'
>>> s[8]
'x'
>>> s[4]
'a'
>>> s[1:4]
'kir'
>>> s[0:3]
'Aki'
>>> s[4:3]
''
>>> s[4:8]
'aChi'
>>> s[3]
'r'
>>> s[-4:]
'Chix'
>>> s[-3:-7]
''
>>> s[-5:-2]
'aCh'
>>> s[-8:-6]
'ki'
>>> s[1:-3]
'kiraC'
>>> s[-6:7]
'raCh'
>>> s[-5:8]
'aChi'
>>> s[3:-3]
'raC'
>>> s[-3:3]
''
>>> x=[1,2,3]
>>> y=["a","b","c"]
>>> z=[1,2,"a","b",3.3,"true","false",true,false]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list'>
>>> type(z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> z=[1,2,3,4,"true","false"]
>>> type(z)
<class 'list'>
>>> a=[1,2,3,4]
>>> b[5,6,7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> b=[5,6,7]
>>> c=a+b
>>> d=a*3
>>> c
[1, 2, 3, 4, 5, 6, 7]
>>> d
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> dir a
  File "<stdin>", line 1
    dir a
        ^
SyntaxError: invalid syntax
>>> dir (a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> fruits=["mango","banana","passion","watermelon"]
>>> fruits.append("pineapple")
>>> fruits.extend("orange","grape")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: extend() takes exactly one argument (2 given)
>>> fruits.append(["pineapple"])
>>> fruits.extend(["grapes","mango"])
>>> fruits
['mango', 'banana', 'passion', 'watermelon', 'pineapple', ['pineapple'], 'grapes', 'mango']
>>> fruits.insert(1,"Avocado")
>>> fruits
['mango', 'Avocado', 'banana', 'passion', 'watermelon', 'pineapple', ['pineapple'], 'grapes', 'mango']
>>> fruits.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'str'
>>> fruits.sort[]
  File "<stdin>", line 1
    fruits.sort[]
                ^
SyntaxError: invalid syntax
>>> fruits.reverse()
>>> fruits
['mango', 'grapes', ['pineapple'], 'watermelon', 'pineapple', 'passion', 'mango', 'banana', 'Avocado']
>>> fruits.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (0 given)
>>> fruits
['mango', 'grapes', ['pineapple'], 'watermelon', 'pineapple', 'passion', 'mango', 'banana', 'Avocado']
>>> fruits.pop()
'Avocado'
>>> len.fruits()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'fruits'
>>> len(fruits)
8
>>> fruits=["mango","banana","orange","ovacado"]
>>> fruits[0]
'mango'
>>> fruits[3]
'ovacado'
>>> fruits[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruits[3:5]
['ovacado']
>>> fruits[3,4 )
  File "<stdin>", line 1
    fruits[3,4 )
               ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> x=[1,2,3,4,5]
>>> for n in x print(n)
  File "<stdin>", line 1
    for n in x print(n)
               ^
SyntaxError: invalid syntax
>>> for n in x:print(n)
... n
  File "<stdin>", line 2
    n
    ^
SyntaxError: invalid syntax
>>> x
[1, 2, 3, 4, 5]
>>> for n in x:print(n*10)
... x
  File "<stdin>", line 2
    x
    ^
SyntaxError: invalid syntax
>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> for n in x:print(n*10)
... 
10
20
30
40
50
>>> for n in x:print(n*n)
... 
1
4
9
16
25
>>> fruits.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
>>> for n in fruits:print(fruits.upper]
  File "<stdin>", line 1
    for n in fruits:print(fruits.upper]
                                      ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> for fruits in fruits:(print.upper]
  File "<stdin>", line 1
    for fruits in fruits:(print.upper]
                                     ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> for fruits in fruit:(print)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruit' is not defined
>>> for f in fruits:print(f.upper())
... 
MANGO
BANANA
ORANGE
OVACADO
>>> for f in fruits:print(f.lower())
... 
mango
banana
orange
ovacado
>>> 
