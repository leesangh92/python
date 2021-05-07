# 빌트인 되어있는 함수(내장 함수, 시스템 (제공)함수, 표준 함수)
'''
dir(__builtins__)

a = [4, 3, 5]
min(a)
max(a)
type(a)
sorted(a)
a.sort()

dir(list)
dir(tuple)
'''

# 사용자 정의 함수
'''
def f1(): # 함수 정의
    pass # 아무 일도 하지 않음
def f2():
    print(' f2... ' )

def f3(x):
    print(x, '가 좋아요')

def f4(x, y):
    print(' {} + {} = {} '.format(x, y, x+y))

def plus(x,y):
    print(' {} + {} = {} '.format(x, y, x+y))
    return None # 기본적으로 생략되어있다

def minus(x, y):
    return x-y

f1() #함수 호출
f2()
f3(100)
f3(100, 500) # 에러 발생(인자 개수 = 매개변수 개수)
f3('BTS')
f4(100, 200)
plus(200, 300)

return_value = minus(300, 200)
print(return_value)

print(minus(300, 200))

print(' 20 - 5 = ', minus(20, 5))
'''
# 구조
'''
def Talk(x, y):
    print(x, '님이', y, '번 말씀하셨다.')

def Aha(x):
    print(x, '누구나 인생은 한 번 뿐이라고.')

print(' Start ')

name = input('이름 : ')
num = int(input('횟수 : '))
          
for i in range(1, num+1):
    Aha(i) 

Talk(name, num)

print(' End ')
'''
# 덧셈만 가능한 계산기
'''
def plus(x,y):
    print(' {} + {} = {} '.format(x, y, x+y))
    return None

def add(x, y):
    return x + y

while True:
    
    number1 = int(input(' 첫 번째 수 : '))

    if number1 == 0:
        break

    number2 = int(input(' 두 번째 수 : '))

    #print(' {} + {} = {}'.format(number1, number2, number1 + number2))
    plus(number1, number2)
    retv = add(number1, number2)
    print(' {} + {} = {}'.format(number1, number2, retv))
'''
# 계산기
'''
def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y

while True:
    n1 = int(input(' 첫 번째 수 : '))
    
    op = input(' [ + (덧셈), - (뺄셈), * (곱셈), / (나눗셈) ] ')
    
    n2 = int(input(' 두 번째 수 : '))

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, ' 은(는) 없는 연산입니다. ')
        break

    print(' {} {} {} = {} '.format(n1, op, n2, res))
'''

# 가변인수 ( 개수가 달라질 수 있다. )
'''
def func(arg1, arg2):
    print(arg1, arg2)

func('korea', 'seoul')

def add1(x):
    print(x + x)

def add2(x, y):
    print(x + y)
    
def add3(x = 100, y = 100, z = 100): # 디폴트 인수
'''
'''나는 값을 더하는 함수다''' # doc string(커서가 깜빡이는 동안 나타나는 말풍선)
'''    
    print(' x = ',  x, ' y = ', y, ' z = ', z)
    #print(x + y + z)

add3(10, 20, 30)
add3(10, 20)
add3(10)
add3()
add3(z=5, x=7, y=3) # 키워드 인수

def call(x = '철수'):
    print(x, '야 놀자!')

def call(name = '철수'):
    print(name, '야 놀자!')
    
call()
call('만수')
call(name = '영희')
'''

'''
def f(x):
    t = x + x # t : 지역 변수
    return t

r = f(5)
print(r)
print(t), print(x) # x, t가 지역 변수이므로 정의되지 않았다는 에러메세지가 뜹니다.
print(f(5))
'''
'''
def Disp(name = '만수르'):
    print(name, '님은 돈이 많아요')

Disp()
Disp('정용진')

def Disp2(x):
    for i in x:
        print(i)
        
def Disp3(x):
    print(x)

def Disp4(*x): # list의 각각의 값이 tuple 형태로 전달
    for i in x:
        print(i, end = ' ')
    
a = [3, 6, 9]
b = a

def Sum(x):
    s = 0
    for i in x:
        s = s + i
        return s

def Sum100(*x):
    s = 0
    for i in x:
        s = s + i
        return s
    
Disp2(a)
Disp3(a)
'''
'''
Disp3(*a) # 각각의 인자를 입력받았기 때문에 인자 개수와 매개변수 개수가 다릅니다.
'''
'''
Disp4(3, 6, 9) # 각각의 인자를 입력받았기 때문에 인자 개수와 매개변수 개수가 다릅니다.

print(id(a), id(b))

print(Sum(a))  
print(Sum([1, 2, 3, 4, 5]))
print(Sum100(*a))
'''


'''
color = {'black' : '검정', 'yellow' : '노랑', 'blue' : '파랑'}
def disp_color(**x):
    for key, value in x.items():
        print(key, value)

print(color['black'], color['yellow'], color['blue']) # 사전 인수
    
disp_color(**color)
disp_color('bk', '검', 'yw', '노', 'bl', '파') # 개수를 같게 해주면?
'''

'''
gg = 11 # 전역 변수

def f1(x):
    gg = 00 # 함수 정의 필드 바깥에 있는 전역변수와 이름이 같지만 다르다
    print(gg, ' x -> ', x*x)

def f2(x, y):
    t = x*y
    print(gg, t)

print(f1(10))
print(f2(100, 300))
print(gg)
'''

'''
gg = 11 

def f1(x):
    global gg # 변수이름을 필드 바깥에서 찾으세요, 전역변수로 지정
    gg = 00 
    print(gg, ' x -> ', x*x)

def f2(x, y):
    t = x*y
    print(gg, t)

print(f1(10))
print(f2(100, 300))
print(gg)
'''

'''
def f():
    print(111)

f()
print(f()) # return값까지 출력
'''

'''
a = [1, 2, 3]

def f(*a): # 디폴트 인수
    print(a)

f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6, 7)

def f(a): 
    print(a)
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6, 7)
'''
# lambda 함수
'''
def f(x):
    for i in range(1, 11):
        f(i)
print((map(f(x), list(range(1, 11)))))

f = lambda x: x*x # lambda 함수, 이름이 없는 함수?
print(list(map(f, range(1,11))))
'''
'''
a1 = list(range(1, 11))
a2 = [i for i in range(1, 11)] # 리스트 정렬식

print(list(map(lambda x: x*x, range(1, 11))))

f= lambda x: x*x
print(list(map(f, range(1, 11))))
'''
