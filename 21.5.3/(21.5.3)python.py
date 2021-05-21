Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> a=[5, 6, 2, 3, 8]
>>> a
[5, 6, 2, 3, 8]

>>> type(a) # 자료형
<class 'list'>

>>> a.sort()
>>> a
[2, 3, 5, 6, 8]
>>> sum(a) # 합
24
>>> min(a) # 최솟값
2
>>> max(a) # 최댓값
8
>>> a
[2, 3, 5, 6, 8]

# 에러, reversed(X), reverse(O)

>>> a.sort(reversed=False)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.sort(reversed=False)
TypeError: 'reversed' is an invalid keyword argument for sort()

>>> a.sort(reverse=False) # 정렬, reverse=False(오름차순)
>>> a
[2, 3, 5, 6, 8]
>>> a.sort(reverse=True) #정렬, reverse=True(내림차순)
>>> a
[8, 6, 5, 3, 2]

# 에러, 문자열 작은 따옴표

>>> b=[서울, 대전, 대구, 부산, 제주]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b=[서울, 대전, 대구, 부산, 제주]
    
NameError: name '서울' is not defined
>>> b=['서울', '대전', '대구', '부산', '제주']
>>> b
['서울', '대전', '대구', '부산', '제주']
>>> b.sort() # ㄱ,ㄴ,ㄷ 순 정렬
>>> b
['대구', '대전', '부산', '서울', '제주']
>>> sum(b) # 문자열 합은 불가능
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sum(b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> keys=['a', 'b', 'c', 'd', 'e'] # 딕셔너리에서 키만 설정
>>> x=dict.fromkeys(keys)
>>> x
{'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
>>> y=dict.fromkeys(keys,1/2/3/4/5) #딕셔너리에서 각각의 키에값을 설정하려 시도
>>> y
{'a': 0.008333333333333333, 'b': 0.008333333333333333, 'c': 0.008333333333333333, 'd': 0.008333333333333333, 'e': 0.008333333333333333}
>>> y=dict.fromkeys(keys,1//2//3//4//5)
>>> y
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> a = {1:'a', 1:'b', 1:'c', 1:'d'} # 딕셔너리에서 중복된 키 값은 가장 오른쪽에 있는 값만 나타남
>>> a
{1: 'd'}
>>> 
