create table kamesh(
first_name varchar(10),
last_name varchar(10),
email varchar(50),
age int,
address varchar(50),
branch varchar(10),
zip char(6),
CGPA decimal(4,4),
);
select * from kamesh;
insert into kamesh(first_name,last_name,email,age,address,branch,zip,CGPA)
values
(1,'Kamesh','Jaiswal','kameshJaiswal123@gmail.com',19,'MIT-CSN','CSE',9.78)