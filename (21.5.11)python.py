Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> a = [i for i in range(1, 101, 2)]
>>> a
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> type(a)
<class 'list'>
>>> aa = (i for i in range(1, 101, 2))
>>> aa
<generator object <genexpr> at 0x00000202FF212660>
>>> type(aa)
<class 'generator'>
>>> next(aa)
1
>>> next(aa)
3
>>> aa.__next__()
5

>>> import sys
>>> k = 10
>>> k1 = 20
>>> k2 = 'koreakorea'

>>> sys.getsizeof(k)
28
>>> sys.getsizeof(k1)
28
>>> sys.getsizeof(k2)
59
>>> 
>>> t1 = [2, 3, 5]
>>> sys.getsizeof(t1)
120
>>> t1 = [2, 3, 5, 7, 9, 11]
>>> sys.getsizeof(t1)
152
>>> a = [i for i in range(1, 101, 2)]
>>> len(a)
50
>>> sys.getsizeof(a)
472
>>> a = [i for i in range(1, 1001)]
>>> sys.getsizeof(a)
8856
>>> b = (i for i in range(1, 101))
>>> sys.getsizeof(b)
112
>>> b = (i for i in range(1, 1001))
>>> sys.getsizeof(b)
112

>>> a = [i for i in range(1, 11)]
>>> sys.getsizeof(a)
184
>>> a = [i for i in range(1, 101)]
>>> sys.getsizeof(a)
920
>>> a = [i for i in range(1, 1001)]
>>> sys.getsizeof(a)
8856
>>> b = (i for i in range(1, 11))
>>> sys.getsizeof(b)
112
>>> b = (i for i in range(1, 101))
>>> sys.getsizeof(b)
112
>>> 
>>> a = [i for i in range(1, 101, 2)]
>>> len(a)
50
>>> sys.getsizeof(a)
472
>>> a2 = iter(a)
>>> sys.getsizeof(a)
472
>>> sys.getsizeof(a2)
48
>>> type(a2)
<class 'list_iterator'>
>>> a[3]
7
>>> a2[3]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a2[3]
TypeError: 'list_iterator' object is not subscriptable
>>> a2.__next__()
1
>>> next(a2)
3
>>> next(a2)
5
>>> next(a2)
7