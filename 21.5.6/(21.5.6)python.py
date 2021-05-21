Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [3, 6, 9]
>>> type(a)
<class 'list'>
>>> a[0]
3
>>> a[1]
6
>>> a[2]
9
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[3]
IndexError: list index out of range # 범위를 벗어남

>>> len(a)
3

>>> a
[3, 6, 9]
>>> b
[1, 2, 3]

>>> a + b
[3, 6, 9, 1, 2, 3]
>>> ab = a + b
>>> ab
[3, 6, 9, 1, 2, 3]

>>> a.extend(b)
>>> a
[3, 6, 9, 1, 2, 3]

>>> len(a)
6
>>> a[5]
3
>>> a[5] = 99
>>> a
[3, 6, 9, 1, 2, 99]
>>> a[6]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[6]
IndexError: list index out of range

>>> a.append(77)
>>> a.append(88)
>>> a
[3, 6, 9, 1, 2, 99, 77, 88]
>>> len(a)
8
>>> a.append(99, 00)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.append(99, 00)
TypeError: list.append() takes exactly one argument (2 given) # 리스트의 형태로 추가
>>> a.append([99, 00])
>>> a
[3, 6, 9, 1, 2, 99, 77, 88, [99, 0]] # 리스트에 리스트 추가
>>> a.extend([11, 22])
>>> a
[3, 6, 9, 1, 2, 99, 77, 88, [99, 0], 11, 22]
>>> a.insert(2, 33)
>>> a.insert(4, 55)
>>> a
[3, 6, 33, 9, 55, 1, 2, 99, 77, 88, [99, 0], 11, 22] # 리스트에 요소 추가

>>> a.pop()
22
>>> a
[3, 6, 33, 9, 55, 1, 2, 99, 77, 88, [99, 0], 11]
>>> 
>>> a.index(3)
0
>>> a.index(55)
4
>>> a.index(99)
7
>>> a.index(00)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.index(00)
ValueError: 0 is not in list # 다중 리스트
>>> a.index(123)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.index(123)
ValueError: 123 is not in list # 리스트 내부에 존재하지 않는 값

>>> a1 = a.pop()
>>> a1
[99, 0]
>>> a1.append(11)
>>> a1
[99, 0, 11]
>>> a1[1] = 22
>>> a1
[99, 22, 11]
>>> a
[3, 6, 33, 9, 55, 1, 2, 99, 77, 88]
>>> a.remove(9)
>>> a
[3, 6, 33, 55, 1, 2, 99, 77, 88]
>>> a.append(99)
>>> a
[3, 6, 33, 55, 1, 2, 99, 77, 88, 99]
>>> a.remove(99)
>>> a
[3, 6, 33, 55, 1, 2, 77, 88, 99]
>>> a.copy()
[3, 6, 33, 55, 1, 2, 77, 88, 99]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given) # 몇 번 입력되었는지 확인하고 싶은 값을 입력해야합니다.
>>> a.count(99)
1
>>> a.del(1)
SyntaxError: invalid syntax # 올바르지 않은 함수 형태
>>> del(a[4])
>>> a
[3, 6, 33, 55, 2, 77, 88, 99]

>>> a.clear()
>>> a
[]

>>> a = [3, 2, 5, 1, 4]
>>> a
[3, 2, 5, 1, 4]
>>> a.sort() # a.sort(reverse = False) 
>>> a
[1, 2, 3, 4, 5]
>>> a.sort(reverse = True)
>>> a
[5, 4, 3, 2, 1]
>>> acopy = a.copy()
>>> acopy
[5, 4, 3, 2, 1]
>>> a.clear()
>>> a
[]
>>> acopy
[5, 4, 3, 2, 1]
>>> a.append(999)
>>> a
[999]
>>> acopy
[5, 4, 3, 2, 1]

============================ RESTART: Shell ===========================
>>> a = [1, 2, 3.14, 9.8, 'ace', 'korea', 3]
>>> a
[1, 2, 3.14, 9.8, 'ace', 'korea', 3]
>>> type(a)
<class 'list'>
>>> len(a)
7
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'float' # 문자열과 실수를 정렬할 수 없다.

>>> b = ['서울', '부산', '인천']
>>> b.sort()
>>> b
['부산', '서울', '인천']

>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(a)
<class 'list'>
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 매직 메서드
>>> a == b
False
>>> a.__eq__(b) 
False

>>> t = (1, 2, 3)
>>> len(t)
3
>>> t[0]
1
>>> t[1], t[2]
(2, 3)
>>> t.index(1)
0
>>> t.index(2)
1
>>> t.index(100)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    t.index(100)
ValueError: tuple.index(x): x not in tuple # 튜플 내에 존재하지 않는 값
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given) # 입력된 횟수를 알고 싶은 값을 입력하세요
>>> t.count(1)
1
>>> t.count(100)
0
>>> t[1] = 99
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    t[1] = 99
TypeError: 'tuple' object does not support item assignment # 튜플요소는 변경할 수 없습니다.

>>> type(t)
<class 'tuple'>
>>> list(t)
[1, 2, 3]
>>> tt = list(t)
>>> tt
[1, 2, 3]
>>> t
(1, 2, 3)
>>> t1 = tuple(tt)
>>> t1
(1, 2, 3)
>>> t
(1, 2, 3)
>>> tt
[1, 2, 3]

>>> i = 100
>>> j = 300
>>> i
100
>>> j
300
# 데이터 맞교환
>>> k = i
>>> i = j
>>> j = k
>>> i
300
>>> j
100
>>> temp = i
>>> i = j
>>> j = temp
>>> i
100
>>> j
300
>>> 
>>> i, j = j, i
>>> i
300
>>> j
100

>>> z = 10, 20, 30 # packing
>>> z
(10, 20, 30)
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z # unpacking
>>> z1
10
>>> z2
20
>>> z3
30
>>> z1, z2 = z
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    z1, z2 = z
ValueError: too many values to unpack (expected 2) # 개수를 맞춰야합니다.

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'i', 'j', 'k', 't', 't1', 'temp', 'tt', 'z', 'z1', 'z2', 'z3']

# 메모리에 저장되어있는 값들을 제거합니다.
>>> del(a, b, i, j, k, t, t1, temp, tt)
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'z', 'z1', 'z2', 'z3']
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> a = {1, 2, 3, 4, 5}
>>> b = {2, 4, 6}
>>> a
{1, 2, 3, 4, 5}
>>> b
{2, 4, 6}
>>> type(a)
<class 'set'>
>>> type(b)
<class 'set'>
>>> a | b # 합집합
{1, 2, 3, 4, 5, 6}
>>> a & b # 교집합
{2, 4}
>>> b - a # 차집합
{6}
>>> a.union(b) # 합집합
{1, 2, 3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
>>> a.intersection(b) # 교집합
{2, 4}
>>> a & b
{2, 4}
>>> len(a)
5
>>> len(b)
3
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable # 집합은 인덱스X

>>> a.add(9)
>>> a
{1, 2, 3, 4, 5, 9}
>>> a.add(1)
>>> a.add(1)
>>> a
{1, 2, 3, 4, 5, 9} # 집합은 중복되는 값이 일일히 저장되지 않는다.
>>> k = []
>>> k.append(1)
>>> k.append(1)
>>> k
[1, 1]
>>> a.remove(1)
>>> a
{2, 3, 4, 5, 9}
>>> a = {1, 2, 3, 4, 5}
>>> a1 = {2, 3}
>>> a
{1, 2, 3, 4, 5}
>>> a1
{2, 3}
>>> a1.issubset(a) # 부분집합
True
>>> a1.issuperset(a)
False
>>> a.issuperset(a1)
True
>>> 
>>> 
>>> d = {'이름' : '강호동', '나이' : 51, '직업' : 'MC'}
>>> type(d)
<class 'dict'>
>>> d['이름']
'강호동'
>>> d['나이']
51
>>> d.keys()
dict_keys(['이름', '나이', '직업'])
>>> d.values()
dict_values(['강호동', 51, 'MC'])
>>> d.items()
dict_items([('이름', '강호동'), ('나이', 51), ('직업', 'MC')])
>>> for key, value in d.items():
	print(key, value)

	
이름 강호동
나이 51
직업 MC
>>> for key, value in d.items():
	print(key, :, value)
	
SyntaxError: invalid syntax
>>> for key, value in d.items():
	print(key, ':', value)

	
이름 : 강호동
나이 : 51
직업 : MC

>>> d[0]
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    d[0]
KeyError: 0

>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d.update({'수입' : 30})
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC', '수입': 30}

>>> d.get('수입')
30
>>> d.popitem()
('수입', 30)
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC'}
>>> a
{1, 2, 3, 4, 5}
>>> 2 in a
True
>>> 2 not in a
False

>>> aaa = a
>>> id(a)
2239990720320
>>> id(aaa)
2239990720320
>>> a is aaa
True
>>> aaa is aaa
True
>>> a is not aaa
False
>>> ac = a.copy()
>>> id(ac)
2239990720992
>>> a is ac
False
>>> True & False
False
>>> True | False
True
>>> True ^ False
True
>>> True ^ True
False
>>> ~True
-2
>>> ~0
-1
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> for i in 1, 2, 3:
	print(i)
	print(i * i)

	
1
1
2
4
3
9
>>> for i in 'korea', 'japan', 'china':
	print(i)
	print(i * i)

	
korea
Traceback (most recent call last):
  File "<pyshell#254>", line 3, in <module>
    print(i * i)
TypeError: can't multiply sequence by non-int of type 'str'
>>> for i in 'korea', 'japan', 'china':
	print(i)
	print(i + i)

	
korea
koreakorea
japan
japanjapan
china
chinachina
	
>>> for i in range(10):
	print(i, end = ' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(100, 0, -5):
	print(i, end = ' ')

	
100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 

>>> Sum = 0
>>> for i in range(1, 10, 1):
	Sum = Sum + i
	print(i, Sum)

	
1 1
2 3
3 6
4 10
5 15
6 21
7 28
8 36
9 45

