'''
def fun1():
    print('fun1 함수입니다.')

def fun2(x):
    print(id(x))
    for i in range(x):
        print('{}번째 fun2 함수 호출'.format(i+1))

def fun3(x, y):
    print('{} + {} = {}'.format(x, y, x+y))

def fun4(x, y, z):
    print('{} + {} + {} ={}'.format(x, y, z, x+y+z))
    return None

def fun5():
    pass

def fun6():
    return 500, 50, 5

def fun7(x, y):
    return x+y

fun1()
fun2(3)
fun3(3, 5)
fun4(2, 3, 5)
fun5()
fun6()
fun7(100, 300)
fun5(100) # TypeError: fun5() takes 0 positional arguments but 1 was given
fun7(100, 300, 500) # TypeError: fun7() takes 2 positional arguments but 3 were given
'''

a = 0

def sum(x):
    a = 0
    for i in range(x + 1):
        a = a + i
        return a

sum(10)
sum(100)
sum(1000)

def Sum(x, y):
    sum = 0
    for i in range(x, y+1):
        sum = sum + i
        return sum

Sum(1, 10)
Sum(1, 100)

def star(x):
    for i in range(x):
        print('*', end="")

star(5)
