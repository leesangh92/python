'''
import sqlite3 as s

con = s.connect('c:\\dd\\adb')
c = con.cursor()

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu, price)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')
c.execute('delete from score where name="한석봉"')

c.execute('select * from lunch')
res = c.fetchall() # 모든 데이터를 클라이언트로 가져온다

print(c.fetchall())

print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())

print('메뉴 가격')

print('**********')

print(res)

for i in res:

    print(i[0],i[1])
    
print('**********')

con.commit()
c.close()
con.close()
'''

'''
## mysql - 연동 
import pymysql as my 

con = my.connect(host='127.0.0.1', user='root', \
    password='password', db='bdb')
c = con.cursor()

#c.execute('create table lunch(menu char(20), price int)')
# c.execute('insert into lunch values("짜장면", 5000)')
# c.execute('insert into lunch values("비빔밥", 8000)')
# c.execute('insert into lunch values("돈까스", 7000)')

c.execute('select * from lunch')

res = c.fetchall()
print(res[0])
print(res[0][0], res[0][1])
print(res[1][0], res[1][1])
print(res[2][0], res[2][1])


print(' 메뉴  가격 ')
print('************')

for i in res:
    print(i[0], i[1])    
print('************')

con.commit()
c.close()

con.close()
'''

## mysql - 연동 
import pymysql as my 

con = my.connect( host='127.0.0.1', user='root', password='wlqQorh10djr', db='kdb')
c = con.cursor()

c.execute('select * from mt')

res = c.fetchall()

# print(res)
# print(res[0])
# print(res[0][0], res[0][1])
# print(res[1][0], res[1][1])

print('************')
print('산이름  해발')
print('************')
for i in res:
    print(i[0], i[1])    
print('************')

con.commit()
c.close()

con.close()
