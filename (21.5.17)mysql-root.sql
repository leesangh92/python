use world;
show tables;
desc city;
select count(*) from city;
select * from city limit 50;
select * from city where CountryCode = 'kor';
select * from city where CountryCode = 'USA';

desc country;
select count(*) from country;
select * from country;

desc countrylanguage;
select count(*) from countrylanguage;
select * from countrylanguage;

select * from city where name in ('seoul', 'new york');
select * from city where countrycode = (select countrycode from city where name = 'seoul');
select * from city where countrycode = 'kor';
select Countrycode from city where name = 'seoul';

select * from city order by population desc limit 10;
select countrycode, name, max(population) from city group by countrycode having max(population) > 9000000 order by max(population) asc;
-- 정해진 순서

select * from city join country on city. Countrycode = Country.code; -- (테이블.필드 이름)
select countrycode from city;
select code from country;

select city.name, city.countrycode, city.population, country.GNP 
from city 
join country
on city.countrycode = country.code;
-- 모델링(테이블 쪼개기), 정규화(테이블 나누기), 릴레이션(테이블 간의 관계)
