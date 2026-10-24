--order by , top offset feth
--****************************************
--Group by,Constraint ( not null , check,default , index , pk, unique   )
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

	select * from Department


	
	select * from department
	order by did asc

	select * from department
	order by did desc

	
	select * from department
	order by ename asc

	select * from department
	order by ename desc

	select * from department
	order by did asc, ename asc
	
	select * from department
	order by gender asc, dept asc

	
	select BusinessEntityID,firstname,LastName from AdventureWorks2025.person.person
	--select * from databasename.schemaname.tablename 

	
	select firstname,LastName from AdventureWorks2025.person.person
	order by FirstName asc 

	select firstname,LastName from AdventureWorks2025.person.person
	order by FirstName asc,lastname desc


--select * from databasename.schemaname.tablename 

	select BusinessEntityID,firstname,LastName 
	from AdventureWorks2025.person.person
	
	
	select top 1 BusinessEntityID,firstname,LastName 
	from AdventureWorks2025.person.person
	
	select top 5 BusinessEntityID,firstname,LastName 
	from AdventureWorks2025.person.person
	
	select top 10 BusinessEntityID,firstname,LastName 
	from AdventureWorks2025.person.person
	
	
	select  top 1 BusinessEntityID,firstname,LastName 
	from AdventureWorks2025.person.person
	order by BusinessEntityID asc 




--highest salary from dept table 
	select * from department
	order by salary desc

	select top 1 * from department
	order by salary desc

--lowest salary from dept table 

	select top 1 * from department
	order by salary asc

	
	select   * from department
	order by salary desc

	
--find highest salary from the table 

	select  top 1 * from department order by salary desc

--find lowest salary from the table 

	select  top 1 * from department order by salary asc

--find 2nd high sal from table

	select    * from department order by salary desc

--2nd high sal =  7500


	select    * from department 
	order by salary desc
	offset 1 rows

--A TOP can not be used in the same query or sub-query as a OFFSET.
	select  top 1  * from department 
	order by salary desc
	offset 1 rows
	
--2nd high sal
	select    * from department 
	order by salary desc
	offset 1 rows				--Skip a row from the table
	fetch  next 1 rows only		--limit a row / same like a top 


--3rd high sal

	select    * from department 
	order by salary desc
	offset 2 rows				--Skip a row from the table
	fetch  next 1 rows only		--limit a row / same like a top 


/*
	top		= limit 
	offset	= skip a row
	fetch	= limit

	top = fetch 


	select top 
	col,col, ....
	from tablename 
	where col=value
	order by col asc, col desc
	offset val rows
	fetch next val rows only

*/