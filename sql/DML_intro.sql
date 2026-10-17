--DDL, drop , schema, dml sleect insert, update, delete, truncate.
---*********************************
--Alter 
	--	drop a column


--Drop 
	--Syntax: Drop table tablename
	Create database sqldemo;
	use sqldemo
	
	drop table Department 


--Drop Database 
	--Syntax: Drop Database Databasename

	Drop Database Demo
	
	Drop Database Atom


--inform the database needs to be deleted 
--idenitify who is coneected to the database 
--internal stored procedure to find connection details
	sp_who2

--remove the connection from the SQL 
	kill 66


	
	Drop Database Atom

	use master
	Drop Database SQL
	Drop Database SQLDEMO

	Drop Database SQL_DEMO

sp_who
Kill 52


sp_who


sp_who2
--*********************************************
--organisation(HR, FIN, SAL, MAR)

CREATE DATABASE org
	use ORG 

--HR
	create table t1 (c1 int , c2 int)
	create table t2 (c1 int , c2 int)
	create table t3 (c1 int , c2 int)
--FIN
	create table t4 (c1 int , c2 int)
	create table t5 (c1 int , c2 int)
	create table t6 (c1 int , c2 int)

--SAl
	create table t7 (c1 int , c2 int)
	create table t8 (c1 int , c2 int)
	create table t9 (c1 int , c2 int)

--MAR
	create table t10 (c1 int , c2 int)
	create table t11 (c1 int , c2 int)
	create table t12 (c1 int , c2 int)

	select * from org


--*********************************************

--dbo=Schema= logical container
--default schema = dbo

--user defined schemas

--default schema = dbo

	--create schema schemaname 
	--create table schemaname.tablename (col datatype, col datatyep,.....)

	CREATE DATABASE Neworg
	use Neworg 

--HR
	create schema HR
	create table HR.t1 (c1 int , c2 int)
	create table HR.t2 (c1 int , c2 int)
	create table HR.t3 (c1 int , c2 int)

	create table t1 (c1 int , c2 int)
	create table t2 (c1 int , c2 int)
	create table t3 (c1 int , c2 int)

--FIN
	create schema FIN
	create table  FIN.t4 (c1 int , c2 int)
	create table  FIN.t5 (c1 int , c2 int)
	create table  FIN.t6 (c1 int , c2 int)

--SAl
	create schema sal
	create table sal.t7 (c1 int , c2 int)
	create table sal.t8 (c1 int , c2 int)
	create table sal.t9 (c1 int , c2 int)

--MAR
	create schema mar
	create table mar.t10 (c1 int , c2 int)
	create table mar.t11 (c1 int , c2 int)
	create table mar.t12 (c1 int , c2 int)
--**************************************************************
	create database DEMO

	use DEMO

	Create  table  Employee  
	(eid smallint , ename varchar(50), age tinyint, gender char(15), salary decimal(10,2))
--********************************
--DML (Data Manipulation Language)

--Select (read)
	--Syntax: Select Column1,column2, column3,.... from table  
	use DEMO
	
	select eid, ename,age , gender, salary from Employee

	select  gender, salary, eid, ename,age from Employee

	select salary from Employee
	
	select gender, salary from Employee

	
	select * from Employee


--Insert(add the records)

--Syntax: 
	--Insert into  tablename(Column1,column2, column3,....) values (val1, val2, val3,.......)
	
	insert into employee (eid, ename,age , gender, salary) values (101, 'alpha',21,'male',8976.45)

	insert into employee (gender, salary, eid, ename,age) values ('male',8976.45,102, 'beta',24)
	
	insert into employee 
	values (103, 'charles',25,'female',98765.45)

	
	insert into Employee  values
	(107,'fox',56,'male',9987),
	(108,'tom',46,'male',7987),
	(109,'delta',78,'male',4987)

--Column name or number of supplied values does not match table definition.


	insert into Employee(eid,salary)  values
	(104,9987)
	
	insert into Employee(eid)  values
	(105)
	
--Data Missing= not available = unknown =absent = NULL		
	insert into Employee  values
	 (Null, null, null, null, null)
	 	
--**************************************
--UPDATE( modify the table-values)
/*Syntax:
	update tablename 
	set column=value,column=value,.....
	where column=value
*/
	update Employee
	set ename = 'priya', age =28, gender ='female'
	where eid =104
	
	update Employee
	set ename = 'jay', age =28, gender =' male', salary =456789
	where eid =105
	
	update Employee
	set ename = 'alex'
	where eid =101
	
	
	update Employee
	set eid=106,ename = 'jay', age =28, gender =' male', salary =456789
	where eid =null           -- this does nothing , as = null dosent make any chnages, is null is the correct syntax
	
	update Employee
	set eid=106,ename = 'jay', age =28, gender =' male', salary =456789
	where eid is null
	
		
	update Employee
	set eid=111,ename = 'jay', age =28, gender =' male', salary =456789
	where eid =101
	
	
	select * from Employee



--never run update , delete without where clause 

	update Employee
	set ename = 'JOHN', gender =' male' 
 
 

--delete (remove a records/ multiple records from table )
	--syntax : delete from tablename where COLUMN=value 
	delete from employee where eid =111

	delete from employee where eid in(102,104,109, 106)
	
	delete from employee 


--Truncate (remove all records from table )
	--Syntax: Truncate table tablename
	
	Truncate table Employee
	
	select * from Employee

