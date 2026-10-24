--Aggregate function, Group by,Constraint ( not null , uk, check,default   )
--*******************************************************
	create database Demo
	
	use demo 
 	
 
	CREATE TABLE Department
	(
		did INT,
		ename VARCHAR(50) ,
		gender VARCHAR(50) ,
		salary INT ,
		dept VARCHAR(50) 
	)
	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'Vince', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance') 
	
	INSERT INTO Department  VALUES
	(16, null,null,null,null)

	select * from Department


--Aggregate function (Count , max , min , avg, sum)

--Count(*)
	select Count (*)   from Department
	select Count (*) as CountRows from Department

--Count(columnname)
	select Count (did) as CountID from Department
	select Count (ename) as CountName from Department

--max (columnname)
	select max (did) as maxval from Department
	select max (ename) as maxval from Department
	select max (salary) as maxval from Department


--min(columnname)
	select min (did) as minval from Department
	select min (ename) as minval from Department
	select min (salary) as minval from Department



--avg sum(numeric column)

	select sum (did) as total from Department
	select sum (salary) as total from Department

	select sum (ename) as total from Department
 	
	
	select sum (did) as total from Department
	where gender ='male'
--AVG

	select Avg (did) as total from Department
	select Avg (salary) as total from Department
	 
	
	select Avg (did) as total from Department
	where gender ='male'


	select Count(*) as COunts,max(salary) as maxvalue,min(salary) as minvalue,sum(salary) as total,avg(salary) as avgval
	from Department


--GROUP BY

--- breaks REsultset into subset
	--Synatx:  select columnname from department group by columnname

	select did, ename,gender,salary,dept from Department

	
	select did  from Department GROUP BY did
	select ename from Department GROUP BY ename
	select salary from Department GROUP BY salary

	select gender from Department GROUP BY gender
	select dept from Department GROUP BY dept

--final all the male and the females and there salaries

	select gender ,sum(salary) as Total from Department GROUP BY gender 
	select dept ,sum(salary) as Total from Department GROUP BY dept

	
	select gender ,Count(*) as Counts from Department GROUP BY gender 
	select dept ,Count(*) as Counts from Department GROUP BY dept
	 
	
	select gender ,Count(*) as Counts,sum(salary) as Total  from Department GROUP BY gender 
	select dept ,Count(*) as Counts,sum(salary) as Total from Department GROUP BY dept



	 
	select 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	where dept is not null		--ignore null values
	GROUP BY dept ,gender
--filter where gender ='male'
	select 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	where gender ='male'
	GROUP BY dept ,gender

--salary total should be greater then 10000
	select 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	where sum(salary) >10000  
	GROUP BY dept ,gender

	
--An aggregate may not appear in the WHERE clause unless it is in a subquery contained
-- in a HAVING clause or a select list, and the column being aggregated is an outer reference.

	select 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	GROUP BY dept ,gender
	having  sum(salary) >10000  

	select 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	GROUP BY dept ,gender
	having  count(*) =3  


	select top 1 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	GROUP BY dept ,gender
	having  count(*) =3  
	order by dept desc

	select top 5 
	dept ,gender 
	,Count(*) as Counts
	,sum(salary) as Total 
	from Department 
	where gender ='male'
	GROUP BY dept ,gender
	having  count(*) =3  
	order by dept desc


--*******************************************


	
	INSERT INTO Department  VALUES
	(null, null, null, null,null),
	(-5, 'Shane', 'Female', -100, 'Finance')


	select * from department  order by did asc


-- Yes, with rules 

	Null		=	Not null
	Duplicate	=	Unique
	out of range = check
	default value = default

--Create table 


	CREATE TABLE NewDept
	(
		did INT not null unique ,
		ename VARCHAR(50)  not null ,
		gender VARCHAR(50)  not null  check (gender in('male','female')),
		salary INT  not null  check (salary >5000),
		phnum bigint not null  unique   check (len(phnum)=10) ,
		dept VARCHAR(50)  not null default 'hr'
	)


	INSERT INTO newdept  VALUES
	( 1,'David', 'Male',  5001, 8214567890,'Sales'),
	( 2, 'Shane', 'female',  5500,7236567890, 'Finance'),
	(3, 'Shed', 'Male', 8000,6734567890, 'Sales'),
	( 4,'Vik', 'female', 7200,9238567890, 'HR')
	
	
--Violation of UNIQUE KEY constraint 
--Cannot insert duplicate key in object

	INSERT INTO newdept  VALUES
	( 1,'David', 'Male',  5001, 8214567890,'Sales')


	
--Cannot insert the value NULL into column
	INSERT INTO newdept  VALUES
	( null,null, null, null, null, null)


--The INSERT statement conflicted with the CHECK constraint 	
	INSERT INTO newdept  VALUES
	( 11,'David', 'Males',  5001, 8204567890,'Sales')

	INSERT INTO newdept  VALUES
	( 11,'David', 'Male',  5001, 70457890,'Sales')


	
	INSERT INTO newdept (did,ename	,gender,	salary,	phnum) VALUES
	( 11,'David', 'Male',  8001, 8204567890)


	INSERT INTO newdept (did,ename	,gender,	salary,	phnum) VALUES
	( 13,'David', 'Male',  8001, 8234567890)


	
	select * from newdept


