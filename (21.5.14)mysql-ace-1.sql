select user();
use mysql; # mysql 데이터베이스는 root 계정이 아니면 접근불가
use acedb;
show tables;
create table s
(
	id int auto_increment primary key,
    name varchar(20),
    kor tinyint,
    eng tinyint,
    math tinyint
);
desc s;

insert into s(name, kor, eng, math) values('이순신',85,87,90);
insert into s(name, kor, eng, math) values('강감찬',75,80,95);
insert into s(name, kor, eng, math) values('한석봉',99,98,99);
insert into s(name, kor, eng, math) values('황진이',35,45,20);
insert into s(name, kor, eng, math) values('안중근',90,85,90);
insert into s(name, kor, eng, math) values('박문수',95,98,96);
insert into s(name, kor, eng, math) values('임꺽정',15,35,45);
insert into s(name, kor, eng, math) values('김정호',90,95,80);
insert into s(name, kor, eng, math) values('정몽주',90,90,95);
insert into s(name, kor, eng, math) values('양주종',50,45,60);

select * from s;
select * from s limit 5;
select * from s where kor > 80;
select * from s where math <= 50;
select * from s where kor > 80 or math <= 50;
select * from s where kor > 80 and math > 80;
