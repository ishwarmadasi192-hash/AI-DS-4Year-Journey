create database demo;
use demo;
create table Employee(eid int,ename varchar(10),age tinyint,gender varchar(10),salary float);

-- add column 
use demo;
alter Employee;
add phnum tinyint;
-- delete column
use demo;
alter Employee;
drop column gender;
--edit datatype of column
use demo;
alter Employee;
alter colummn phnum bigint;