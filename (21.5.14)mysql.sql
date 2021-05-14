create database rootdb;
use rootdb;
show databases;
create table book 
(-- 필드이름  자료형
	title  char(30),    -- 고정폭
    author varchar(30), -- var : 가변폭
    price  int          -- tinyint, smallint, mediumint, int, bigint(숫자 범위를 지정하여 메모리 할당량을 줄일 수 있다)
);
    
desc book;
insert into book values('주식하는 마음', '홍진채', 17000);
insert into book values('MySQL이다', '우재남', 30000);
insert into book values('주식하는 마음', '홍진채', 17000); -- primary 명령어, 중복되는 내용을 처리하는 명령어
insert into book values('주식하는 마음', '홍진채', 17000);
select * from book;

show tables;
alter table book rename bb;
alter table bb add press char(20);
desc bb;
select * from bb;

delete from bb where price = 17000;
select * from bb;

drop table bb;




use world;
show tables;
desc city; -- 5 fields
select count(*) from city;

select * from city limit 3;
select * from city limit 100, 10; -- 100번째부터 10개, 페이징할 때 주로 사용

select count(*) from country;
desc country;
select * from country;
