
>>> man = ['이순신', '황진이', '한석봉']
>>> job = ['군인', '가수', '공무원']
>>> zip(man, job)
<zip object at 0x00000237C49EDF40>
>>> list(zip(man, job))
[('이순신', '군인'), ('황진이', '가수'), ('한석봉', '공무원')]
>>> a = list(zip(man, job))
>>> a
[('이순신', '군인'), ('황진이', '가수'), ('한석봉', '공무원')]
>>> dict(a)
{'이순신': '군인', '황진이': '가수', '한석봉': '공무원'}
>>> a.keys()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.keys()
AttributeError: 'list' object has no attribute 'keys'
>>> a1 = dict(a)
>>> a1.keys()
dict_keys(['이순신', '황진이', '한석봉'])
>>> a1.values()
dict_values(['군인', '가수', '공무원'])
>>> a1.items()
dict_items([('이순신', '군인'), ('황진이', '가수'), ('한석봉', '공무원')])




>>> for i, j in emunerate(man):
	print (j)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    for i, j in emunerate(man):
NameError: name 'emunerate' is not defined
>>> for i, j in enumerate(man):
	print (j)
	
이순신
황진이
한석봉
>>> for i, j in enumerate(man):
	print (i, j)
	
0 이순신
1 황진이
2 한석봉
>>> enumerate(man)
<enumerate object at 0x00000237C2C5B240>
>>> list(enumerate(man))
[(0, '이순신'), (1, '황진이'), (2, '한석봉')]
>>> dict(list(enumerate(man)))
{0: '이순신', 1: '황진이', 2: '한석봉'}
