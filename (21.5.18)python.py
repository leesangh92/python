Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a * 2
[1, 2, 3, 1, 2, 3]
>>> a + 2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a + 2
TypeError: can only concatenate list (not "int") to list
>>> a / 2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a / 2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> a - 2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a - 2
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> score = [20, 50, 60, 30, 40]
>>> sum(score)
200
>>> avg(score)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    avg(score)
NameError: name 'avg' is not defined
>>> sum(score) / len(score)
40.0
>>> a
[1, 2, 3]
>>> b = [4, 5, 6]
>>> b
[4, 5, 6]
>>> c = [a, b]
>>> len(c)
2
>>> c[1][1]
5
>>> t = [i * 3 for i in range(1, 11)]
>>> t
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> len(t)
10
>>> t[:]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> t[3:]
[12, 15, 18, 21, 24, 27, 30]
>>> t[:5]
[3, 6, 9, 12, 15]
>>> t[4:6]
[15, 18]
>>> Tot = 0
>>> for i in range(len(t)-1):
	Tot += t[i]

	
>>> Tot
135
>>> for i in range(len(t)):
	Tot += t[i]

	
>>> Tot
300
>>> Tot = 0
>>> for i in range(len(t)):
	Tot += t[i]

	
>>> Tot
165
>>> 2 ** 8
256
>>> 2 ** 16
65536
>>> 2 ** 32
4294967296
>>> 2** 64
18446744073709551616
>>> x1 = 20
>>> x2 = 50
>>> x1.__add__(50)
70
>>> 10.__add__(50)
SyntaxError: invalid syntax
>>> (10).__add__(50)
60
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> c
[[1, 2, 3], [4, 5, 6]]
>>> sum([0])
0
>>> sum(c[0])
6
>>> 