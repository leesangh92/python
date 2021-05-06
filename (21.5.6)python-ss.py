'''
ss = []
with open('c:\\dd\\ss.txt', 'r', encoding = 'utf8') as file:
    for i in range(10):
        ss.append(file.readline()) # 한 줄씩 읽어들이기
        print(ss)
'''
'''
ss = []
with open('c:\\dd\\ss.txt', 'r', encoding = 'utf8') as file:
    for i in range(10):
        ss.append(file.readline().split()) # 각 줄의 각각의 요소를 나누어 읽어들이기
        
        print(ss)
'''
'''
ss = []
with open('c:\\dd\\ss.txt', 'r', encoding = 'utf8') as file:
    for i in range(5):
        ss.append(file.readline().split())
        
        ss[i][1] = int(ss[i][1])
        ss[i][2] = int(ss[i][2])
        ss[i][3] = int(ss[i][3])

        total = ss[i][1] + ss[i][2] + ss[i][3]
        avg = total / 3

        print(ss)
        print(total)
        print(avg)
'''
ss = []
with open('c:\\dd\\ss.txt', 'r', encoding = 'utf8') as file: # 파일 불러오기
    for i in range(10):
        ss.append(file.readline().split())

        total = 0
        avg = 0
        
        ss[i][1] = int(ss[i][1]) # 불러올 때 기본적으로 문자열 자료형으로 불러오므로 연산자를 사용하기 위해 정수형으로 바꿔주기
        ss[i][2] = int(ss[i][2])
        ss[i][3] = int(ss[i][3])

        total = ss[i][1] + ss[i][2] + ss[i][3] # 각 학생의 점수 총합

        avg = total / 3 # 각 학생의 평균

    for i in range(10):
        total_1 = total_2 = total_3 = 0 # 값의 초기화
        avg_1 = avg_2 = avg_3 = 0
        
        total_1 = total_1 + ss[i][1] # 각 과목의 점수 총합
        total_2 = total_2 + ss[i][2]
        total_3 = total_3 + ss[i][3]

        avg_1 = total_1 / len(ss) # 각 과목의 평균
        avg_2 = total_2 / len(ss)
        avg_3 = total_3 / len(ss)
       
        print(ss[i][0], '총점', total_1 + total_2 + total_3, sep = ' / ', end = '\n')
        print('      ', '평균', (total_1 + total_2 + total_3) / 3 , sep = ' / ', end = '\n\n')
print('**과목 총점', total, sep = ' / ', end = '\n')
print('**과목 평균', avg, sep = ' / ', end = '\n\n\n')

