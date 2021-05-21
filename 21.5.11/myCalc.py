## 초간단 계산기

from myModule import Add, Sub, Mul, Div
# 모듈과 같은 디렉토리 안에 있도록 한다. 

print(__name__, 'myCalc')

while True:
    print(' ** 간단 계산기 ** ')
    print(' -> [종료 : 0]')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break
    
    op = input(' [ +, - * / ] : ')
    
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
        print(op, '없는 연산입니다.')

    print(' {}  {}  {} = {}'.format(n1, op, n2, res))
