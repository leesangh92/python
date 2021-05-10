Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
	return x + y

>>> a = [1, 2, 3, 4]
>>> sum(a)
10
>>> def mySum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i
	return Sum

>>> mySum(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mySum(a)
  File "<pyshell#11>", line 4, in mySum
    Sum = Sum + i
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> mySum(1, 2, 3, 4)
10
>>> mySum(*a)
10


>>> def Add2(x = 30, y = 50):
	return x + y

>>> Add2(3)
53
>>> Add2(100, 200)
300
>>> Add2()
80
>>> Add2(y = 100, x = 200)
300

>>> 
