Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> dir() # 사용 가능한 매직매서드와 매서드를 확인할 수 있다. 
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

>>> a = input("입력")
입력100
>>> a
'100'
>>> type(a)
<class 'str'>

# 자료형이 올바르지 않음
>>> a + 100
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a + 100
TypeError: can only concatenate str (not "int") to str

>>> int(a) + 100
200
>>> a = int(input('정수를 입력하세요 : '))
정수를 입력하세요 : 5
>>> a = int(input('정수를 입력하세요 : '))
정수를 입력하세요 : 10
>>> a
10

>>> city = input('어디서 오셨나요 : ')
어디서 오셨나요 : 서울
>>> a = float(input('실수 입력 : '))
실수 입력 : 2.534
>>> print(a, city)
2.534 서울

>>> print(' aa \t bb \t cc \n dd \t ee \a ff \b gg ')
 aa 	 bb 	 cc 
 dd 	 ee  ff  gg
 
>>> print("서울은 좁아요""아주 좁아요"'정말 좁아요')
서울은 좁아요아주 좁아요정말 좁아요
>>> print("서울은 좁아요 \t" "아주 좁아요 \n" '정말 좁아요')
서울은 좁아요 	아주 좁아요 
정말 좁아요

>>> age = 30
>>> name = '빌 게이츠'
>>> print(name, '님은', age, '세')
빌 게이츠 님은 30 세
>>> print(' %s, %d ' %(name, age))
 빌 게이츠, 30 
>>> print(' %s 님은 %d 세 ' %(name, age))
 빌 게이츠 님은 30 세

# 자리 순서가 다르다
>>> print(' %d, %s ' %(name, age))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(' %d, %s ' %(name, age))
TypeError: %d format: a number is required, not str

>>> print(' [%d] [%10d] [%-10d] ' %(5, 5, 5))
 [5] [         5] [5         ] 
>>> print(' [%d] [%10d] [%-10d] ' %(987654321, 987654321, 987654321))
 [987654321] [ 987654321] [987654321 ] 
>>> print(' {} {} '.format(10, 'seoul'))
 10 seoul 
>>> print(' {} {} {} '.format(10, 3.14, 'seoul'))
 10 3.14 seoul

# 개수가 다르다
>>> print(' {} {} {} '.format(10, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(' {} {} {} '.format(10, 'seoul'))
IndexError: Replacement index 2 out of range for positional args tuple

# 인덱스를 생략하면 순서대로, 인덱스를 수정하여 순서를 변경할 수 있다. 
>>> print(' {0} {1} {2} '.format(10, 3.14, 'seoul'))
 10 3.14 seoul 
>>> print(' {2} {0} {1} '.format(10, 3.14, 'seoul'))
 seoul 10 3.14 
>>> print(' {0} {0} {0} '.format(10, 3.14, 'seoul'))
 10 10 10 
>>> print(' [{0}] [{0}] [{0}] '.format(10, 3.14, 'seoul'))
 [10] [10] [10] 
>>> print(' [{:20}] [{:10}] [{:3}] '.format(10, 3.14, 'seoul')) #표시되는 자리 수
 [                  10] [      3.14] [seoul] 
>>> print(' [{:3}] [{:10}] [{:20}] '.format(10, 3.14, 'seoul'))
 [ 10] [      3.14] [seoul               ] 
>>> print(' [{:>3}] [{:>10}] [{:>20}] '.format(10, 3.14, 'seoul')) # 정렬
 [ 10] [      3.14] [               seoul] 
>>> print(' [{:<3}] [{:<10}] [{:<20}] '.format(10, 3.14, 'seoul'))
 [10 ] [3.14      ] [seoul               ] 
>>> print(' [{:<3}] [{:^10}] [{:>20}] '.format(10, 3.14, 'seoul')) # 가운데 정렬
 [10 ] [   3.14   ] [               seoul] 
>>> print(' [{:<3}] [{:^7}] [{:>20}] '.format(10, 3.14, 'seoul')) # 홀수 자리 수의 가운데 정렬을 왼쪽으로 치우침 
 [10 ] [ 3.14  ] [               seoul] 
>>> print(' [{:<3}] [{:.3f}] [{:>20}] '.format(10, 3.14, 'seoul')) # 소수 자리 수 
 [10 ] [3.140] [               seoul] 
>>> print(' [{:<3}] [{:.10f}] [{:>20}] '.format(10, 3.14, 'seoul'))
 [10 ] [3.1400000000] [               seoul]
 
>>> print(' [%f], [%.2f], [%.10f]'.format(5.2, 5.2, 5.2)) # list []
 [%f], [%.2f], [%.10f]
>>> print(' %f, %.2f, %.10f ' % (5.2, 5.2, 5.2))
 5.200000, 5.20, 5.2000000000 
>>> print(' %f, %.2f, %.10f ' % (5.2, 5.269234, 5.2)) # 소수 자리 수가 정해진 곳까지 반올림해서 표시
 5.200000, 5.27, 5.2000000000 
>>> print(' %f, %.2f, %.10f ' % (5.2, 5.242234, 5.2))
 5.200000, 5.24, 5.2000000000 

>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	print(i, end = ' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
	print(i, end = '\t') # \t : tab 

	
0	1	2	3	4	5	6	7	8	9	
>>> for i in range(0, 10, 2):
	print(i)

	
0
2
4
6
8

# 시작값을 정해줘야 함
>>> for i in range(10, 2):
	print(i)

	
>>> for i in range(1, 10, 2):
	print(i, end = ' ')

	
1 3 5 7 9 
>>> for i in range(0, 10, 3):
	print(i, end = ' ')

	
0 3 6 9 
>>> Sum = 0
>>> for i in range(1, 11):
	Sum = Sum + i

	
>>> Sum
55
>>> for i in range(1,11):
	Sum = Sum + i

>>> Sum
110 # 이전에 계산해서 결과로 나온 Sum의 값에 합해진 값이 나온다.

>>> Sum = 0 # 따라서 값을 초기화 시켜주어야한다. 
>>> for i in range(1, 11):
	Sum = Sum + i

	
>>> Sum
55

>>> Sum1 = 0.0
>>> for i in range(100)
SyntaxError: invalid syntax
>>> for i in range(100):
	Sum1 = Sum1 + 0.1

>>> Sum1
9.99999999999998 # 소수점 계산에 대한 오차, 아날로그 데이터를 디지털 데이터로 변화하면서 생기는 오

>>> print(' %f ' %Sum1) # %f를 사용함으로써 표현되는 소수점 자리 수는 6자리
 10.000000
 
>>> a = int(input(' 정수 : '))
 정수 : 10
>>> b = int(input(' 정수 : '))
 정수 : 30
>>> print(a, b, a+b)
10 30 40
>>> a, b = input(' 정수 2개를 입력하세요 : ').split()
 정수 2개를 입력하세요 : 10 30
>>> print(a, b, a+b)
10 30 1030 # 입력받은 자료형은 기본적으로 문자열

>>> file = open(' c:\\dd\\aa.txt ', 'r', encoding = 'utf8')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    file = open(' c:\\dd\\aa.txt ', 'r', encoding = 'utf8')
OSError: [Errno 22] Invalid argument: ' c:\\dd\\aa.txt ' # 파일디렉토리는 띄어쓰기 유의할 것

>>> file = open('c:\\dd\\aa.txt', 'r', encoding = 'utf8')
>>> print(file.read()) #read() 함수는 읽기 전용
5.4 화요일
날씨 : 비

>>> file1 = open('c:\\dd\\bb.txt', 'w', encoding = 'utf8') # 'w' : 덮어쓰기
>>> file1.write('파이썬을 배웁니다. \n') # write() 함수로 파일을 수정합니다. 
12 # 입력받은 문자 수(파이썬을 배웁니다. \n) \n은 자리바꿈으로 하나의 문자로 취급
>>> file1.write('매일매일 공부합니다. \n')
13
>>> file.close()
>>> file1.close() # close() 함수로 파일을 종료해야 저장됩니다.

>>> file2 = open('c:\\dd\\bb.txt', 'a', encoding = 'utf8') # 'a' : append, 추가
>>> for i in range(5):
	name = input(' 출석자 : ')
	file2.write(name)

	
 출석자 : 훈0
2 # 입력받은 문자 수
 출석자 : 훈1
2
 출석자 : 훈2
2
 출석자 : 훈3
2
 출석자 : 훈4
2
>>> file2.close()

#형변환 함수 
>>> str(1000)
'1000'
>>> int('3333')
3333
>>> int('30')
30
>>> str('22')
'22'
>>> float(45)
45.0
>>> float('국민')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float('국민')
ValueError: could not convert string to float: '국민'
>>> float(id('국민'))
2132869162256.0
>>> a = [2, 4, 6, 8, 10]
>>> b = (1, 2, 3)
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> sum(a)
30
>>> sum(b)
6
>>> max(a)
10
>>> min(a)
2
>>> max(b)
3
>>> min(b)
1
>>> mean(a) # 평균은 Panda에서...
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mean(a)
NameError: name 'mean' is not defined

>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> k = 20
>>> dir(k)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

>>> k+30
50
>>> k.__add__(30)
50

# 괄호를 넣어줘야 한다. 
>>> k.__add__30 # 30 -> (30)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    k.__add__30
AttributeError: 'int' object has no attribute '__add__30'

>>> k == 60
False
>>> k.__eq__(60)
False
>>> k != 60
True
>>> k.__ne__(60)
True
>>> k = 'korea'
>>> type(k)
<class 'str'>
>>> k[0]
'k'
>>> k[1]
'o'

# 설정되어있지 않은 인덱스
>>> k[5]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    k[5]
IndexError: string index out of range

# 오른쪽에서 왼쪽 방향으로 인덱스 찾기
>>> k[-1]
'a'
>>> k[-2]
'e'
>>> k[-5]
'k'
>>> k
'korea'

# 해당 문자가 존재하는 인덱스 찾기
>>> k.find('k')
0
>>> k.find('o')
1
>>> k.find('T')
-1
>>> k.rfind('T')
-1
>>> k.rfind('k')
0

>>> k2 = k * 3
>>> k2
'koreakoreakorea'
>>> k2.find('a')
4
>>> k2.rfind('a')
14
>>> k2.count('a')
3
>>> k2.count('o')
3
>>> k2.count('R')
0
>>> k2.count('e')
3

>>> k2.startswith('R')
False
>>> k2.startswith('k')
True
>>> k2.startswith('p')
False
>>> k2.startswith('e')
False
>>> k2.endswith('a')
True
>>> k2.endswith('b')
False

>>> k2
'koreakoreakorea'
>>> k2.upper()
'KOREAKOREAKOREA'
>>> k2
'koreakoreakorea'
>>> k3 = k2.upper()
>>> k3
'KOREAKOREAKOREA'
>>> k3.lower()
'koreakoreakorea'
>>> s = '   seoul   '
>>> s
'   seoul   '
>>> k
'korea'
>>> k2
'koreakoreakorea'
>>> len(k)
5
>>> len(k2)
15
>>> len(s)
11
>>> s.strip()
'seoul'
>>> s.lstrip()
'seoul   '
>>> s.rstrip()
'   seoul'
>>> 'T'.isalpha()
True
>>> '0'.isalpha()
False
>>> '5'.isalpha()
False
>>> '$'.isalpha()
False
>>> '7'.isnumeric()
True
>>> '$'.isnumeric()
False
>>> 'A'.isnumeric()
False
>>> 'A'.isalnum()
True
>>> '6'.isalnum()
True

>>> s = "seoul"
>>> print(s, "가 좋아요")
seoul 가 좋아요
>>> s.replace('e', 'E')
'sEoul'
>>> s
'seoul'
>>> b1 = "서울이 좋아요"
>>> b2 = b1.replace("서울", "부산")
>>> b1, b2
('서울이 좋아요', '부산이 좋아요')
>>> bc = "kbs mbc sbs ebs ytn"
>>> bc
'kbs mbc sbs ebs ytn'
>>> bc2 = bc.upper()
>>> bc2
'KBS MBC SBS EBS YTN'
>>> type(bc)
<class 'str'>
>>> type(bc2)
<class 'str'>
>>> bc3 = bc2.split()
>>> bc3
['KBS', 'MBC', 'SBS', 'EBS', 'YTN']
>>> type(bc3)
<class 'list'>
>>> type(bc3)
<class 'list'>
>>> len(bc3)
5
>>> bc4 = "kbs/mbc/sbs"
>>> bc4
'kbs/mbc/sbs'
>>> bc5 = bc4.split('/')
>>> bc5
['kbs', 'mbc', 'sbs']
>>> bc4 = "kbs:mbc:sbs"
>>> bc4
'kbs:mbc:sbs'
>>> bc5 = bc4.split(':')
>>> bc5
['kbs', 'mbc', 'sbs']

>>> a = 'apple'

# 문자열 + 정수
>>> a + 4
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    a + 4
TypeError: can only concatenate str (not "int") to str
>>> a * 3
'appleappleapple'
>>> b = 'banana'
>>> b
'banana'
>>> a + b
'applebanana'
>>> b * 4
'bananabananabananabanana'

# 문자열 사이에 공백 넣기           
>>> a '\t' + b
SyntaxError: invalid syntax
>>> a "\t" + b
SyntaxError: invalid syntax
>>> a "end = ' '" + b
SyntaxError: invalid syntax
>>> a (end = ' ') + b
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    a (end = ' ') + b
TypeError: 'str' object is not callable

>>> a = 'apple'
>>> b = ' banana' # 공백을 문자열에 포함시킨다
>>> a + b
'apple banana'

>>> b.partition(a)
('banana', '', '')
>>> b.partition('a')
('b', 'a', 'nana')
