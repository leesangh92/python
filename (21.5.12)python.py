'''
dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

help()



print('**********')
print('안녕하세요')

a = [3, 5, 6]
print("king" + "ace")
print("king" * 3)

try:
    a + 2
except (IndexError, TypeError):
    print('Sorry')

try:
    a[2] / 0
except ZeroDivisionError as msg:
    print(msg)

print("안녕히 계세요")
print('*' * 10)
'''

'''
# Epoch 및 Unix 타임 스탬프 변환 참조(1970.1.1 0시 기준)

import time as t
help(t)
print(t.time())

# gmtime : 그린위치 표준 시
t1 = t.gmtime()
print('{} / {} / {}'.format(t1.tm_year, t1.tm_mon, t1.tm_mday))

t1 = t.gmtime()
print('{}시 {}분 {}초'.format(t1.tm_hour, t1.tm_min, t1.tm_sec))

t2 = t.localtime()
print('{}시 {}분 {}초'.format(t2.tm_hour, t2.tm_min, t2.tm_sec))

print(t1.tm_zone)


import datetime as d
d.datetime.now()

n = d.datetime.now()
print('{}시 {}분 {}초'.format(n.hour, n.minute, n.second))


import calendar as cal
now = cal.calendar(2021)
print(now)

print(cal.month(1992, 8))
'''

from urllib import request as req 
import datetime as d 
import bs4

r =	req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108") 

soup = bs4.BeautifulSoup(r, "html.parser") 
now	= d.datetime.now()


print("=" *	30)
print("* {}년 {}월 {}일 날씨 정보 * ".format(now.year, now.month, now.day))
print("=" * 30) 
print("  도시     날 씨    온  도  ") 
print("=" * 30) 

for	i in soup.select("location"):				
    name = i.select_one("city").string				
    wf   = i.select_one("wf").string				
    tmn  = i.select_one("tmn").string				
    tmx	 = i.select_one("tmx").string								

    print("{:>4s} {:>7s} {}도 ~ {}도".format(name, wf, tmn, tmx))

print("=" * 30)
