select user();
show databases;
select now();

/* root의 고유 권한
create database mydb;
drop database mydb;
*/

use acedb;
show tables;

create table if not exists Man
(
	name char(20),
    year int
);

desc Man;

show tables;

alter table Man add habit char(20);
desc Man;
alter table Man drop habit;
/*
alter table Man drop year;
alter table Man add year int;
*/

insert into Man(name, year) values('kim', 2000);
insert into Man(name, year) values('choi', 1995);
insert into Man(name) values('park');
insert into Man(name) values(23);
insert into Man(year, name) values(22, 'lee');

select * from Man;

delete from Man where name = 'kim';
delete from Man; -- 데이터만 지운다, table은 남아있다

show tables;

-- drop table Man; -- table을 지운다

alter table Man rename Person; -- table 이름 변경

/* -- Access denied: you need (at least one of) the CREATE USER privilege(s) for this opertaion 에러
create user aa@'%' identified by '0000';
grant all privileges on acedb.* to aa@'%' with grant option;
flush privileges;
*/





use acedb;

show tables;

drop table s;

create table if not exists s
(
	id int auto_increment primary key,
    name varchar(20),
    kor tinyint,
    eng tinyint,
    math tinyint
);

insert into s(id, name, kor, eng, math) values(101, '이순신',85,87,90);
insert into s(name, kor, eng, math) values('강감찬',75,80,90);
insert into s(name, kor, eng, math) values('한석봉',99,98,99);
insert into s(name, kor, eng, math) values('황진이',35,45,20);
insert into s(name, kor, eng, math) values('안중근',90,85,90);
insert into s(name, kor, eng, math) values('박문수',95,98,96);
insert into s(name, kor, eng, math) values('임꺽정',15,35,45);
insert into s(name, kor, eng, math) values('김정호',90,95,80);
insert into s(name, kor, eng, math) values('정몽주',90,90,95);
insert into s(name, kor, eng, math) values('양주종',50,45,60);

desc s;
select count(*) from s;
select * from s;

select name, eng from s;

select name, eng from s limit 5;
select name, eng from s limit 2, 3;

select name, eng from s order by name;
select name, eng from s order by name asc; -- asc 기본값
select name, eng from s order by name desc;

select name, eng from s order by kor desc;
select name, eng, math from s order by kor desc;
select name, eng, math from s order by eng desc, math asc; -- 영어 점수가 같을 때 수학 점수로 오름차순 정렬

select name as '이름', kor as '국어' from s;
select min(kor), max(kor), sum(kor), avg(kor) as '국어' from s; -- 집계 함수

select name, (kor + eng + math) as '총점' from s;
select name, (kor + eng + math) as '총점', (kor + eng + math) / 3 as '평균' from s;

create table if not exists s1
(
	name char(20),
    total int,
    avg float
);

insert into s1
	select name, (kor + eng + math), (kor + eng + math) / 3 from s;

show tables;
select * from s1;

select * from s1 where total >= 250;
select * from s1 where avg >= 90;
select * from s1 where avg <= 60;
SELECT * FROM s1 WHERE(70 <= avg) AND (avg <= 90); 
-- select * from s1 where 70 <= avg <= 90; 는 에러
select * from s1 where avg between 80 and 90; -- 80, 90 포함

select * from s1 where name = '이순신';

insert into s1(name) values('이몽룡');
insert into s1(name) values('이율곡');

select * from s1 where name LIKE '이%';
/*
select * from s1 where name = '이*';
select * from s1 where name include '이';
*/
select * from s1 where name LIKE '%이';
select * from s1 where name LIKE '양_종';
select * from s1 where total is null;
select * from s1 where total is not null;

select trim('     kkk     ');
select ltrim('     kkk     ');
select rtrim('     kkk     ');
