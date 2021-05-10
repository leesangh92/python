# 'ctrl + /' 로 선택 문장 주석 처리

# class Korea(object): ## Korea class 선언

#     def __init__(self, city, pop): # 멤버 함수, 생성자 함수, self에 객체의 id 값이 저장된다. 
#         self.city = city
#         self.pop = pop
#         print('Korea __init__ : 생성자 / ', self.city, 'id = ', id(self))

#     def __del__(self): # 멤버 함수, 소멸자 함수
#         print('Korea __del__ : 소멸자 / ', self.city, 'id = ', id(self))

#     def __str__(self):
#         return " {}인구는 {}만 명 ".format(self.city, self.pop)

#     def disp_korea(self): # 멤버 함수
#         print(self.city, '인구는 ', self.pop, '만 명', '\n', 
#               '/', self.city, 'id = ', id(self)) 

#     def get_city(self):
#         return self.city

#     def get_pop(self):
#         return self.pop
        
#     def set_city(self, city):
#         self.city = city

#     def set_pop(self, pop):
#         self.pop = pop

# print('##################################################')

# def ff(): # 함수
#     print('나는 ff 함수다')

# ff()

# k1 = Korea('서울시', 950) # k1 객체 생성
# k2 = Korea('부산시', 700)
# k2.pop = 360 # k2 pop값 변경, 보통 이렇게 값을 변경하지 않고 멤버 함수를 만들어 수정한다.

# k1.disp_korea()
# k2.disp_korea()

# k1.city = '수원시'
# k1.pop = 110
# k2.city = '대구시'
# k2.pop = 120

# print(k1.get_city(), k1.get_pop())
# print(k2.get_city(), k2.get_pop())

# print('k1 -> ', id(k1))
# print('k1 -> ', type(k1))

# print(k1) # 객체를 선언하면 __str__ 함수를 호출한다.
# print(k1.__str__())



class It(object):

    def __init__(self, company, employee): # 인수 입력받기, 생성자 함수 생성
        self.company = company
        self.employee = employee

    def __str__(self): # 문자열 출력
        return ' {}은(는) {}명 근무'. format(self.company, self.employee)

    def disp_It(self): # 출력
        print(' {}은(는) {}명 근무'. format(self.company, self.employee))

    def get_company(self): # 회사 이름 불러오기
        return self.company

    def get_employee(self): # 사원 수 불러오기
        return self.employee

    def set_company(self, company): # 회사 이름 변경하기
        self.company = company

    def set_employee(self, employee):# 사원 수 변경하기
        self.employee = employee

    def __add__(self, num): # 연산자 중복, 재 정의, 매직 메서드 생성
        self.employee = self.employee + num

    def __sub__(self, num):
        self.employee = self.employee - num

    def __eq__(self, other):
        if self.company == other.company and self.employee == other.employee:
            return True
        else:
            return False

It1 = It('google', 56000)
It2 = It('facebook', 47000)

print(It1)
print(It2)

It1.disp_It()
It2.disp_It()

print(It1.get_company(), '의 직원은', It1.get_employee(), '명')
print(It2.get_company(), '의 직원은', It2.get_employee(), '명')

It1.set_company('samsung')
It1.set_employee(96000)

print(It1.get_company(), '의 직원은 ', It1.get_employee(), '명')
print(It2.get_company(), '의 직원은', It2.get_employee(), '명')

print(It1 == It2)
print(It1 is It2)
#print(It1 < It2) # 에러, 문자열은 대소 비교 불가
It1 + 100 # 기본적으로 문자열과 숫자의 덧셈 뺄셈은 불가능하지만 사원 수의 변경 사항을 나타내는 함수를 만들어 줌으로써 가능하게 해준다
It1.disp_It()
It1 - 200
It1.disp_It()

It3 = It2 # 표시되는 내용은 같지만 id값은 다르다 
It2.disp_It()
It3.disp_It()

print(It2 == It3) # 기본적으로 문자열과 숫자가 같더라도 False로 표기 되므로 표기되는 것이 같으면 같은 것이라는 함수를 만들어 줘야한다
print(It2 is It3)
print(id(It2), id(It3))

It33 = It('facebook', 47000)
It2.disp_It()
It33.disp_It()
print(It2 == It33) # 표시되는 값이 같으면 함수를 통해 같다고 표시되게끔 만들었다
print(It2 is It33) # 하지만 id 값은 다르다
print(id(It2), id(It33))
# 함수를 지우면 메모리에서 지워진다.

