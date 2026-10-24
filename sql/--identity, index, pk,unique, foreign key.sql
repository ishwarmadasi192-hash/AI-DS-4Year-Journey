--identity, index, pk,unique, foreign key
--********************************************
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
	

--identity (seed, increment)
	

	use Demo


	create table tokens (sno int identity(1,1),ename char(100))

	insert into tokens 
	values('a')

--An explicit value for the identity column in table 'tokens' can only be specified when a column list is used and IDENTITY_INSERT is ON.
	
	insert into tokens 
	values(15,'b')

	
	insert into tokens 
	values('b')
	insert into tokens 
	values('c')

	insert into tokens 
	values('d')

	insert into tokens 
	values('e')
--disable identity 
	set  IDENTITY_INSERT tokens on
	
	insert into tokens(sno,ename) 
	values(19,'qq')
	
	insert into tokens(sno,ename) 
	values(29,'ew')
	insert into tokens(sno,ename) 
	values(00,'ew')
	insert into tokens(sno,ename) 
	values(1,'ew')


	insert into tokens 
	values('e')


--Enable identity 
	set  IDENTITY_INSERT tokens off


		insert into tokens 
	values('e')

	select * from tokens


--*****************************************************

--index 

	select did from Department

	--id=7

--Execution plan= Cntrl+M

	select did from Department where did =7


--create index

--Clustered index 
	--Sort and store data  in  (existing & new records)
	--1 clustered index in 1 table
	-- improve the speed of read when searching

	select * from Department


--Clustered index =did

--Syntax: Create Clustered index indexname on tablename (Columnname) 
	Create Clustered index CI_DID on Department (did)
	
	
	select did from Department where did =7
	
	select  ename  from Department where ename = 'will'

--Cannot create more than one clustered index on table 	
	Create Clustered index CI_Ename on Department (ename)

	
--NON CLUSTERED  INDEX 
	--999 non clustered index in 1 table
	--Improve the speed of read when searching


--Syntax: Create NonClustered index indexname on tablename (Columnname) 
	Create NonClustered index NCI_Ename on Department (ename)

	select  ename  from Department where ename = 'will'


	Create NonClustered index NCI_three on Department (ename,salary,dept)

	select ename,salary,dept  from department 
	where 	ename='Kate' and salary=7500 and dept='IT'
	
--**************************************************
--unique key  (Unique) 
	--NON CLUSTERED INDEX (SEEK FASTER)
	--999 UK IN 1 TABLE

--Primary key (Unique + Not null) 
	-- Column (set of column)
	--1 pk in table (1 CLUSTERED INDEX (SORT & STORE, SEEK FASTER))
--***********************************************

create table test 
(
id int primary key 
, phnum int unique
)





insert  into test values
(107,3945678)


insert  into test values
(105,753322)



insert  into test values
(null,98645678)

insert  into test values
(986456,null)


select * from test

--**************************************************
	CREATE TABLE Customer (
	CID INT primary key ,  
	CustomerName VARCHAR(100),
	Email VARCHAR(100) unique 
	)

	-- Create Product table
	CREATE TABLE Products (
	PID INT unique , 
	ProductName VARCHAR(100),
	Price DECIMAL(10,2)
	)

	-- Create OrderTable with foreign keys to Customer and Product

	CREATE TABLE OrderTable (
	OrderID INT  ,
	CustomerID INT,
	ProductID INT,
	Quantity INT,
	OrderDate DATE ,
	foreign key (ProductID) references Products(Pid),
	foreign key (CustomerID) references customer(cid)
	)






	
	
--primary key to foreign key 
--refrential integrity(always add the data in the the primary key table first)


-- Insert records into Customer
	INSERT INTO Customer VALUES 
	(1, 'John Doe', 'john@example.com'),
	(2, 'Jane Smith', 'jane@example.com'),
	(3, 'Alice Brown', 'alice@example.com'),
	(4, 'Robert White', 'robert@example.com'),
	(5, 'Emily Green', 'emily@example.com')

-- Insert records into Products
	INSERT INTO Products VALUES 
	(1, 'Laptop', 1200.00),
	(2, 'Smartphone', 800.00),
	(3, 'Tablet', 400.00),
	(4, 'Monitor', 300.00),
	(5, 'Keyboard', 50.00)

-- Insert records into OrderTable
	INSERT INTO OrderTable VALUES 
	(1, 1, 1, 1, '2025-06-01'),
	(2, 2, 3, 2, '2025-06-02'),
	(3, 3, 2, 1, '2025-06-03'),
	(4, 4, 5, 4, '2025-06-04'),
	(5, 5, 4, 1, '2025-06-05') ,
	(6, 1, 2, 1, '2025-06-10'),
    (7, 1, 3, 2, '2025-06-11'),
    (8, 2, 1, 1, '2025-06-12'),
    (9, 3, 5, 3, '2025-06-13'),
    (10, 4, 4, 1, '2025-06-14');


	
--cascading integrity(delete should happen in the foreign key table first)

	delete from  Customer
	delete from Products
	delete from OrderTable

    
	select * from  Customer
	select * from Products
	select * from OrderTable














































