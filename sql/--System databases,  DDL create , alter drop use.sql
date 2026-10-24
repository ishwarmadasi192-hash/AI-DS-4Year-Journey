--System databases,  DDL create , alter drop use 
--************************************
--self learning
	https://learn.microsoft.com/en-us/sql/relational-databases/databases/system-databases?view=sql-server-ver17
 
	https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16
	
	https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver16
	
	https://www.sqlservercentral.com/articles/json-in-microsoft-sql-server-a-comprehensive-guide


--************************************
--System Databases

/*	master:(critical)
		Instance-level metadata, including logins, linked servers, 
		endpoints, configuration settings, and the location of 
		every other database. The instance cannot start without it.
	
	model: 
		Template for every new database, including tempdb at each restart. 
		Its recovery model, file sizes, and objects are inherited.
		--size, count, path 
	create database demo2 
 
	msdb: 
		SQL Server Agent data (jobs, schedules, alerts, operators), 
		backup and restore history, 
		Database Mail, and the SSIS package store (legacy).
	
	tempdb:(critical)
		Temp tables, table variables, sort and hash spills, and the version store. 
		It is recreated at every restart and cannot be backed up.
	

	
	Resource (mssqlsystemresource): 
	Hidden and read-only. It holds the system objects that appear 
	in the sys schema of every database. It is not visible in SSMS 
	and cannot be backed up with 
	BACKUP DATABASE; only a file-level copy of the .mdf and .ldf works.

*/
--***********************************************

--least used 

--DDL
--Create database 
	Syntax: Create database DatabaseName
	
	Create database Demo

	Create database SQL

	Create database Atom

	Create database Demo

	Create database [1A]


	Create database [learn sql]

	
	Create database SQL_DEMO
--*****************************************
Create table 


--Syntax: Create table tablename(columnnme  datatype,columnnme  datatype ,columnnme  datatype,............... )
--Task 
	--Create a table  Employee with columns: (eid, ename, age, gender, salary)

--master to demo 


	use Demo

	Create  table  Employee  (eid int, ename varchar(10), age tinyint, gender char(10), salary float)

	

--Task to create table department (did, ename , age , gender, salary)

	Create  table  department  (eid int, ename varchar(10), age tinyint, gender char(10), salary float)

	
	use SQLdemo

	Create  table  department  (eid int, ename varchar(10), age tinyint, gender char(10), salary float)

--****************************************************

--Modify the table 

--Alter to add a new column to an existing table 
--n=1024

/*Syntax:
	alter table tablename 
	add columnname datatype,columnname datatype,.....
*/
	use Demo
	
	alter table Department  
	add phnum int , email tinyint


	
--Alter to drop a column 
/*Syntax:
	alter table tablename 
	drop column columnname,columnname
*/ 

	use Demo
	
	alter table Department  
	drop column ename

	
	use Demo
	
	alter table Department  
	drop column gender





	
--Alter to modify the datatype of a column
/*Syntax:
	alter table tablename 
	alter column columnname datype
*/ 

	alter table Department  
	alter column phnum bigint

































































