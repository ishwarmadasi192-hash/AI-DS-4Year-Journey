---Where  and , or , in , not , null, betwee, like 

--********************************************************

use AdventureWorks2025

select * from Person.Person



--Search 
--where column  = value

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=8

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName='ken'

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where ModifiedDate='2020-02-17 00:00:00.000'


	
-- Not equal (!=   or <> )
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
		where BusinessEntityID != 1
		
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
		where firstname  != 'Roberto'



-- Greater than or equal to(>=  )

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
		where BusinessEntityID >= 20500


-- Less than or equal to(<= )

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
		where BusinessEntityID <= 10




	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=767 and FirstName='Thierry'


--*********************************************************************
--Where columnName =value AND columnName =value and columnName =value AND columnName =value ......


	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=767 and FirstName='Thierry'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=767 and FirstName='Thierry'and ModifiedDate='2023-05-30 00:00:00.000'

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=767 and FirstName='Thierry'and ModifiedDate='2023-11-30 00:00:00.000'

	
--Where columnName =value or columnName =value or columnName =value or columnName =value ......
--Column based search operation	


	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=1 or  BusinessEntityID=111 or  BusinessEntityID=21 or  BusinessEntityID=31

	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName ='junk value' or 
	FirstName ='bali' or 
	FirstName =	'Terri' or 
	FirstName =	'Roberto' or 
	FirstName =	'Rob' or 
	FirstName =	'Gail' or 
	FirstName =	'Jossef'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=767 and FirstName='Thierry'or ModifiedDate='2023-11-30 00:00:00.000'
--*************************************************************
--WHERE COLUMN  IN (VALI, VAL2, VAL3 ,....)	

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID in(1,2,3,4,5,7,8,9,10)
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	WHERE FirstName in ('Ken','bali','Terri','Roberto','Rob','Gail','Jossef')

--WHERE COLUMN  not IN (VALI, VAL2, VAL3 ,....)	

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID not in(1,2,3,4,5,7,8,9,10)
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	WHERE FirstName in ('Ken','bali','Terri','Roberto','Rob','Gail','Jossef')

	
	
--*********************************************************
--WHERE COLUMN is null , is not null

	select BusinessEntityID,firstname,MiddleName,ModifiedDate from Person.Person
	where MiddleName is null	--find null values	

	select BusinessEntityID,firstname,MiddleName,ModifiedDate from Person.Person
	where MiddleName is not null--ignore null values	

	
	

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID=1 or  BusinessEntityID=111 or  BusinessEntityID=21 or  BusinessEntityID=31

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID in(1,2,3,4,5,7,8,9,10,100)


	
--*************************************************
--where  between  range value1 and value2 


	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where BusinessEntityID between 1and 100


	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where ModifiedDate between '2019-12-12' and '2020-02-23'


	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName ='A'



	
---Where like % _


	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName  like 'A%'

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName  like 'An%'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName  like 'Ana%'

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where FirstName  like 'Anav%'

--*************************************************

	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where lastname   like '%ed'


	

	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where lastname   like '%tom%'

	
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where firstname   like '_'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where firstname   like '__'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where firstname   like '___'
	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where firstname   like '____'


	
	select BusinessEntityID,firstname,LastName,ModifiedDate from Person.Person
	where firstname   like '_A%'