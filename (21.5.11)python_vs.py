# CUR_YEAR = 2021 # 전역 변수

# class Date(object):
#     def __init__(self, year, month):
#         self.year = year
#         self.month = month
#         print('Date __init__ ')

#     def __del__(self):
#         print('Date __del__ ')

#     def disp_Date(self):
#         print('{}년 {}월'.format(self.year, self.month))

# class Man(Date): # 상속받기
    
#     cnt = 0 # 지역 변수, class 변수

#     @staticmethod # @ : 장식자(데커레이터)
#     def get_cnt1():
#         return Man.cnt
    
#     @classmethod
#     def get_cnt2(cls):
#         return Man.cnt

#     def __init__(self, name, year, month): # 생성자(constructor), 객체 생성 시 자동 호출
#         super().__init__(year, month)
#         self.name = name
#         Man.cnt += 1
#         self.age = CUR_YEAR - year + 1

#     def __del__(self): # 소멸자(destructor), 객체 소멸 시 자동 호출
#         Man.cnt -= 1
#         super().__del__()
#         print('Date __del__ ')

#     def __str__(self): # 객체 출력 시 자동 호출, 함수 재정의, 기본값은 객체의 id 값 리턴
#         return '{}님은 {}살'.format(self.name, self.age)

#     def disp_Man(self):
#         print('{}님은 {}살'.format(self.name, self.age))
#         super().disp_Date() # Date class의 메서드 호출

#     # 메서드 중복(method overload)
#     def A1(self,x):
#         return x + x
    
#     def A1(self, x, y):
#         return x + y
        
# m1 = Man('손흥민', 1992, 7)
# m2 = Man('이강인', 2001, 2)

# m1.disp_Man()




# print('start')

# a = [1, 2, 3, 4, 5]

# try:
#     a[10] = 10
#     "korea" + 4
#     4 / 0
# # except IndexError as msg:
# #     print(msg)
# # except TypeError as msg:
# #     print(msg)
# # except ZeroDivisionError as msg:
# #     print(msg)
# except (IndexError, TypeError, ZeroDivisionError):
#     print('셋 중 하나')
# else:
#     print('IndexError, TypeError, ZeroDivisionError 가 아니다')
# finally:
#     print('에러와 상관없이 무조건 실행')

# print('end')





import os

while True:
    print('1. 메모장')
    print('2. 계산기')
    print('3. 그림판')
    print('4. 크롬')
    print('0, 종료')

    sw = input(' 선택해 주세요. [   ] \b\b\b\b')

    if sw == '0':
        print('안녕히 계세요.')
        break

    if sw == '1':
        os.system('notepad')
    elif sw == '2':
        os.system('calc')
    elif sw == '3':
        os.system('mspaint')
    elif sw == '4':
        os.system('start chrome')
    else:
        print(sw, '없는 메뉴')
    
    