Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fun1():
    pass

>>> def fun2():
    print(' fun2입니다. ')

>>> def fun3(x):
    print(' fun3입니다. ' )

    
>>> def fun4(x, y):
    for i in range(y):
        print(x, '님 반가워요.')

        
>>> def fun5(x):
    return x * x

>>> def add(num1, num2):
    print(' {} + {} = {} '.format(num1, num2, num1 + num2))
    return 5, 10, 300

>>> fun1()
>>> fun2()
 fun2입니다. 
>>> fun3()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fun3()
TypeError: fun3() missing 1 required positional argument: 'x'
>>> TypeError: fun3() missing 1 required positional argument: 'x'fun3(5)
SyntaxError: invalid syntax
>>> fun3(5)
 fun3입니다. 
>>> fun4(5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fun4(5)
TypeError: fun4() missing 1 required positional argument: 'y'
>>> fun4('철수',5)
철수 님 반가워요.
철수 님 반가워요.
철수 님 반가워요.
철수 님 반가워요.
철수 님 반가워요.
>>> fun5()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fun5()
TypeError: fun5() missing 1 required positional argument: 'x'
>>> fun5(5)
25
>>> fun5(5, 3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fun5(5, 3)
TypeError: fun5() takes 1 positional argument but 2 were given
>>> ret5 = add(10, 20)
 10 + 20 = 30 
>>> ret5
(5, 10, 300)
>>> type(ret5)
<class 'tuple'>
>>> 
