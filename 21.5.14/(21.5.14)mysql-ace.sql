use acedb;
show tables;
create table score(name char(30), kor int, math int, eng int);
desc score;
select * from score;
select count(*) from score;

insert into score values('이순신',85,87,90);
insert into score values('강감찬',75,80,95);
insert into score values('한석봉',99,98,99);
insert into score values('황진이',35,45,20);
insert into score values('안중근',90,85,90);
insert into score values('박문수',95,98,96);
insert into score values('임꺽정',15,35,45);
insert into score values('김정호',90,95,80);
insert into score values('정몽주',90,90,95);
insert into score values('양주종',50,45,60);

select * from score;
select count(*) from score;
select * from score limit 3, 3; # 3번째 부터 3개
desc score;
select name, kor from score;
select name, kor from score limit 5; # 5개
select name as '이름', kor as '국어' from score;

select (kor + eng + math) as '총점' from score;
select (kor + eng + math) / 3 as '평균' from score;
select name as '이름', (kor + eng + math) as '총점', (kor + eng + math) / 3 as '평균' from score; # 저장은 안되어있는 상태
select name as '이름', kor as '국어', eng as '영어', math as '수학' from score;
select name as '이름', kor as '국어', eng as '영어', math as '수학', (kor + eng + math) as '총점', (kor + eng + math) / 3 as '평균' from score;

delete from score; -- Edit - Preferences - SQL Editor 탭 가장 아래 Safe updates(rejects updates...) 체크 박스 해제

select * from score;

select * from score order by name asc; -- desc : 내림차순

-- drop table score;
