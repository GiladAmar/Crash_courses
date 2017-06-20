#############################################
Author 			= "Gilad Amar"				#
Email 			= "giladamar@gmail.com"		#
Created 		= "2016"				#
Last_Modified  	= "04/11/2016"				#
#############################################

/* 
	WELCOME TO THE SQL INTRODUCTORY CODE.
	This is part of a multi-line comment. 
*/
 /* Warning: the following pseudo-code will make you cry
 	A safety pig has been provided for your benefit:
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
*/

--DATA TYPES:
	String	VARCHAR(1024)	-- Any characters, with a maximum field length of 1024 characters.
	Date/Time	TIMESTAMP	-- Stores year, month, day, hour, minute and second values as YYYY-MM-DD hh:mm:ss.
	Number DOUBLE PRECISION -- Numerical, with up to 17 significant digits decimal precision. 
							-- Does not support commas, or currency symbols.
	Boolean	BOOLEAN			-- Only TRUE or FALSE values

--Columns can be cast to another type(within reason) with:
	CAST(expression AS [data type])
	column_name::[data type]
	CONVERT([data type], expression)

--TODO Items:
	-- Partition by and rank over
	--
decimal(10,5)
-----------------

	USE [Handover]
-----------------
	CREATE PROCEDURE [dbo].[stp_run_feature_generator]
		AS
	BEGIN 
		sql_script_here
	END

----------------------

SELECT * FROM EMPLOYEE
MINUS
SELECT * FROM EMPLOYEE WHERE ID > 2
-----------------
SELECT * FROM EMPLOYEE WHERE ID IN (2, 3, 5)
INTERSECT
SELECT * FROM EMPLOYEE WHERE ID IN (1, 2, 4, 5)
-----------------
--Cannot compare nulls
effectively True, False AND NULL
NULL is NULL
anything evaluated WITH NULL results IN 'Unknown'

-----------------
SELECT nth highest
	SELECT TOP (1) Salary FROM
	(
	    SELECT DISTINCT TOP (10) Salary 
	    FROM Employee 
	    ORDER BY Salary DESC
	) AS Emp ORDER BY Salary
-----------------
-- Cant use alias to order group etc 
-----------------
-- Group functions can be nested to a depth of two.
-----------------
--IN ANY All
-----------------
--Can insert NULL of just not insert if cell should be empty
-----------------
--The MERGE statement allows conditional update or insertion of data into a database table. It performs an UPDATE if the rows exists, or an INSERT if the row does not exist.
-----------------
-- A DROP TABLE statement cannot be rolled back.
-----------------
-- Avoid division by 0
COALESCE(dividend / NULLIF(divisor, 0), 0)
-----------------
--SQL INJECTION
print("With Hack: \n")
Name = "Robert'; DROP TABLE students;--"
print("SELECT * FROM students WHERE Name = '%s'" % Name)
-----------------
-- dividing ints to make float
	SELECT 2 / 3
	-> 0
	SELECT 2 * 1.0 / 3
	-> 0.666666
	SELECT AVG(numbers) FROM table_name
	-> 2.0
	SELECT AVG(numbers * 1.0) FROM table_name
	-> 1.8
-----------------
------------------------------Query Types------------------------------
------------------------------SELECT------------------------------
SELECT [ TOP x ] <fields> 			-- STANDARD SELECT STRUCTURE	
									-- Can also select the top 50%
									-- SELECT TOP 50 PERCENT
FROM <table> 
[ INNER JOIN <table> 
	ON <fields> ]
[ WHERE <condition> ]				-- Restricts records before the groups are summarised.
[ GROUP BY <field> 		
[ HAVING <condition> ] ]			-- Restricts summarised records after the groups are summarised.
[ ORDER BY <fields> ];  
[ LIMIT y]

------------------------------CREATE------------------------------
CREATE TABLE table_name				-- Create a new table or view
(
	column_name1 data_type(size),  										-- Create column of datatype and size
	LastName varchar(255) NOT NULL, 									-- Cannot have null values
	P_Id int NOT NULL CHECK (P_Id>  0) IDENTITY(1, 1) UNIQUE PRIMARY KEY,	-- Create a unique Primary Key that must be >0 and not null
																		-- the key automatically increase by one from IDENTITY(1, 1)
	CONSTRAINT pk_PersonID PRIMARY KEY (P_Id,LastName)					-- Add a named constraint, pk_Person_ID, such that list of columns forms Primary Key
	FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)							-- Ensure local key must exist as primary key on foreign table
	City varchar(255) DEFAULT 'Sandnes'									-- Set default values for column
); 	

CREATE UNIQUE INDEX index_name			-- Create an index for a table
										-- does not have to be unique
ON table_name (LastName, FirstName)


CREATE OR REPLACE VIEW view_name AS 	-- Create an on-the-fly view of a table 
										-- (OR REPLACE will recreate if already view by that name)

------------------------------INSERT------------------------------
INSERT INTO tblPlayers 			-- Add values in row to table
			(firstName, lastName) 
	   VALUES (‘Douglas’, ‘Adams’);

------------------------------ALTER------------------------------
ALTER TABLE table_name					-- Change the structure of a table (fields)u
	ADD column_name data_type 			-- Add a column of a certain datatype
	DROP COLUMN column_name 			-- Delete column
	ALTER COLUMN column_name data_type 		-- Change column datatype
	ADD PRIMARY KEY (P_Id) 				-- Add a Primary key
	DROP PRIMARY KEY 					-- Remove a Primary Key

	ADD CONSTRAINT pk_PersonID PRIMARY KEY (P_Id, LastName)		-- Make Primary key from list of columns (constraint named "pk_PersonID")
	ADD CONSTRAINT chk_Person CHECK (P_Id > 0 AND City = 'Sandnes')	-- Add constraints to multiple columns
	ADD CONSTRAINT uc_PersonID UNIQUE (P_Id, LastName) 				-- Add Uniqueness constraint to list of columns
	DROP CONSTRAINT uc_PersonID										-- Delete a constraint

	ADD FOREIGN KEY (P_Id)											-- Require that key column in table is in foreign table too
		REFERENCES Persons(P_Id)

	ALTER COLUMN City SET DEFAULT 'SANDNES'							-- Add a default value for a column
	ALTER COLUMN City DROP DEFAULT 									-- Delete default value for a column

------------------------------UPDATE------------------------------
UPDATE tblPlayers					-- Change values in Table
	SET handicap = 17 
	WHERE membNo = 2;	

------------------------------DELETE------------------------------
DELETE FROM tblPlayers 				-- Delete rows from table
	WHERE membExpire < NOW();
TRUNCATE TABLE CUSTOMERS 			-- Empty the  Table 

------------------------------DROP------------------------------
DROP TABLE IF EXISTS table_name;	-- Delete table if it exists(Some SQL versions only)
									-- Otherwise 
DROP TABLE [ETL].[Sub_Data_new]
IF OBJECT_ID('ETL.Respondent_Data', 'U') IS NOT NULL 

DROP INDEX table_name.index_name	-- Drop index from a table

DROP VIEW 							-- Drop a view

------------------------------COMPLETE SELECT SAMPLE STATEMENT------------------------------

SELECT TOP 100 * + (5 * 2) / 2.5 ,year, month,	-- Can use arithmetic operations (+, - ,* ,/ ) with columns BODMAS brackets
		a.*,									-- Select all columns from Table alias a
		name 				AS newName,			-- Give column new name, can be used later in query. Use AS "Title with Spaces" for spaces.
		COUNT(artist) 		AS num_artists, 	-- Counts no. in artist column NOT nulls.
		SUM(earnings) 		AS profit,			-- Sums column, treats nulls as 0.
		AVG(group_members) 	AS avg_band_size	-- Find column average, completely ignores nulls (doesn't treat like zeros).
		MIN(year) 			AS earliest_year,	-- Column minimum. Handles dates, numbers and strings.
		MAX(albums_sold) 	AS max_sold,		-- Column maximum. Handles dates, numbers and strings
		DISTINCT(month)  	AS uniq_months,		-- DISTINCT returns unique entries in month column.
												-- DISTINCT(year, month) will return unique pairs.
												-- "SELECT DISTINCT * ..." will return unique rows.
												-- DISTINCT performs slowly.
		UPPER(),								-- Return string in uppercase
		LOWER(),								-- Return string in lowercase
		ROUND(Price, 0),						-- Round column to 0 decimals
		COALESCE(UnitsOnOrder, 0),				-- Returns first non null argument (here used to replace nulls with zero)
		ISNULL(UnitsOnOrder, 0),				-- Returns 0 if UnitsOnOrder is NULL
		STDEV(group_members) AS std_dev_members,-- Standard Deviation
		VAR(group_members) AS variance_members,	-- Variance

		CASE
    		
    		ELSE  'We Do Not Have Records For This Customer'
    		END AS 'result';

		CASE WHEN weight > 250 THEN 'over 250' 	-- IF THEN ELSE statement 
             WHEN weight > 200 AND weight <= 250 THEN '201-250'
             WHEN weight > 175 AND weight <= 200 THEN '176-200'
             WHEN EXISTS(
        				SELECT 1 
        				FROM call_records
        				WHERE account = @accountnumber
    					) 
             	THEN  'We Have Records of this Customer'
             ELSE '175 or under' 				-- ELSE is optional
             END AS weight_group

	-- FROM song_schema.song_data as artists
	FROM songs_schema.songs songs a 	--Can be given an alias, here just "a".
	  	JOIN artist_schema.artist earnings b
	    	ON songs.artist = earnings.artist
	    	AND companies.name = investments.company_name 					-- Joining on more than one key, even if unneccesary is much faster.
	    	AND acquisitions.company_permalink != '/company/1000memories', 	-- Additional condition for merger --EVALUATED BEFORE where
/*FOR INNER JOIN - returns only overlap in data
		If multiple matches, all matches will be returned as seperate rows
		If no matches no row is returned
		If two same named columns they will haveb the same resultant data. 
		Can be renamed as:
			 	SELECT 	players.school_name AS players_school_name,
			        	teams.school_name 	AS teams_school_name
			   	FROM benn.college_football_players players
			   		JOIN benn.college_football_teams teams
			     		ON teams.school_name = players.school_name
FOR OUTER JOIN - 	Can return unmatched rows from either set (LEFT/RIGHT JOIN) 
					or FULL OUTER JOIN returns unmatched rows from both.
FOR FULL OUTER JOIN - Returns a left, inner and right join.
*/
/*
--To exclude some rows where they appear in another table 
	SELECT Table_1.* FROM Table_1
		LEFT JOIN Table_2
			ON Table_1.id = Table_2.id
	WHERE Table_2.id IS NULL
	-- Can be used similarly to ONLY Take shared rows with IS NOT NULL
*/

		tutorial.crunchbase_companies companies
	  	LEFT JOIN tutorial.crunchbase_acquisitions acquisitions
	    	ON companies.permalink = acquisitions.company_permalink
/*	    	
	In this join, companies data is either left alone or added to.
	It is a CONVENTION to use LEFT JOIN over JOIN, not logically neccesary.
*/
	WHERE month = 1  					-- =, !=, >, <, >=, <=
										-- or month = 'january' in single quotes, operators now refer to alphabetic order.
		AND 'day' LIKE '%day' 			-- Case-sensitive.
		OR 'day' ILIKE '%dAY' 			-- Case-insensitive 	% is a multi-wildcard character.
										-- 'day' LIKE 'Mo_day' 	_ is a single wildcard character.
		OR 'day' LIKE '[mtw]%day'		-- [charlist]  Sets range of characters to match eg. [abc] or [a-c]
										-- [!charlist] Set range of characters to not match eg. [!abc]
		AND 'artist' IN ('Taylor Swift', 'Ludacris', 1, 2, 3)
		AND year BETWEEN 1999 AND 2016 	-- BETWEEN is inclusive of bounds. 
										-- Can use NOT BETWEEN to get outside range
		AND band IS NOT NULL 			-- band != NULL Won't work(arithmetic on a str)
										-- Only with conditional statement.
		OR band = 'Gotye'
		OR (band = 'MUSE' AND  'album' = 'Absolution')

	GROUP BY year, month 			-- Creates only unique year, month rows with the remaining columns
									-- grouped into vectors which can be operated on.
									-- Order doesn't matter
									-- GROUP BY 1,2 means group by the first two columns mentioned after SELECT; those created.

	HAVING MAX(earnings) > 1000000 	-- Like a where statement for which groups are selected APPLIED AFTER Grouping

	ORDER BY year DESC, artist 		-- Ascending by default when no DESC.
									-- Artist is second column to sort by.

	LIMIT 100 						-- Result only cut down to limit at end of operation(so doesn't affect results)
				
--/////////////////////////////END OF SAMPLE SELECT STATEMENT////////////////////////////////////


------------------------------GROUPING------------------------------
/*
	For when grouping by different conditions.
	Create the groups with a multiple case then statement.
	Perform aggregates on groupings given by:
	Group BY(1)
	1 refers to the first output column in the after Select
*/
SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' 
        	END AS year_group,
        COUNT(1) AS count
FROM benn.college_football_players
GROUP BY 1


------------------------------STACK SELECT STATEMENTS------------------------------
-- Must have same number of columns, and data types
-- Column names don't have to be the same
 SELECT *
 FROM tutorial.crunchbase_investments_part1
 UNION 						-- Removes rows from Table 2 identical to any in Table 1
 							-- UNION ALL joins all the rows regardless
 SELECT *
 FROM tutorial.crunchbase_investments_part2

------------------------------STRING_EXPRESSIONS------------------------------
LEN(string_var)									-- Return the length of the string
LEFT(string_var, index) 							-- Take from char 1 to index
MID(string_var) 									-- Take mid char
RIGHT(string_var, index) 							-- Take from char 1 to index
LENGTH('stringy')									-- Get length of string
REPLACE (str1, str2, str3) 							-- In str1, find where str2 occurs, and replace it with str3.
TRIM( [ <LOCATION> [remstr] FROM ] str) 			-- <LOCATION> can be either LEADING, TRAILING, or BOTH. 
													-- If <remstr> pattern is not gieven white spaces are removed.
CONCAT (str1, str2, str3, ...)						-- Concat all strings
SUBSTRING(Res_QnA.Question_str, index_1, index_2) 	-- Take substring between index_1 and index_2
CHARINDEX('-', QnA.Question_str)						-- Find Position of character in string

------------------------------MATHEMATICAL_EXPRESSIONS------------------------------
IGN(x)		-- Sign of input x as -1, 0, or 1
MOD(x, y)	-- (same as x%y)
FLOOR(x)	-- Largest integer value that is less than or equal to x
CEIL(x)		-- Smallest integer value that is greater than or equal to x
POWER(x, y)	-- x raised to the power of y
ROUND(x)	-- x rounded to the nearest whole integer
ROUND(x, d)	-- x rounded to the d number of decimal
SQRT(x)		-- Square-root value of x


------------------------------LOGICAL EXPRESSIONS------------------------------
IS NULL 
IS NOT NULL  
IIF(handicap <= 15, ‘Good’, ‘Bad’)

------------------------------PIVOTING-----------------------------------------
--WHERE Year is categorical column, and Salesamount is to be aggregated.
--Static

SELECT   [Country], [2005],   [2006], [2007],   [2008], [2009],   [2010]
FROM   [dbo].[PivotExample] 
PIVOT
(
       SUM(SalesAmount)
       FOR [Year] IN ([2005], [2006], [2007], [2008], [2009], [2010])
) AS P


--Dynamic


	--Declare necessary variables
	DECLARE   @SQLQuery AS NVARCHAR(MAX)
	DECLARE   @PivotColumns AS NVARCHAR(MAX)
	 
	--Get unique values of pivot column  
	SELECT   @PivotColumns= COALESCE(@PivotColumns + ',', '') + QUOTENAME(Year)
	FROM (SELECT DISTINCT Year FROM [dbo].[PivotExample]) AS PivotExample
	 
	--Create the dynamic query with all the values for 
	--pivot column at runtime
	SET   @SQLQuery = 
	    N'SELECT Country, ' +   @PivotColumns + '
	    FROM [dbo].[PivotExample] 
	    PIVOT( SUM(SalesAmount) 
	          FOR Year IN (' + @PivotColumns + ')) AS P'

	--Execute dynamic query
	EXEC sp_executesql @SQLQuery

-----------------------------------Dynamic SQL ---------------------------
BEGIN 
	--Declaring variables
	DECLARE @source_table varchar(max)
			,@start_date DATETIME
			,@data_threshold numeric

	SET	@source_table 	= '[db_ucg].[dbo].[tbl_data_dictionary_201602]'
	SET @table_name 	= '[Gil].[dbo].[tbl_Processed_Data_testFeb]'
	SET @start_date 	= '2016-02-01 00:00:00.000'							
	SET @data_threshold = SELECT 1024 / 10      -- CAN USE SQL HERE

	BEGIN
		--Make command String
		SET @cmd = 'SELECT * INTO ' + @table_name + ' FROM ' + @source_table 
		-- Execute comman string with neccesary input. "string of parameters", parameter_1, parameter_2, ...
		exec sp_executesql @cmd,N'@table_name nvarchar(50), @start_date DATETIME, @data_threshold numeric', 
								@table_name, @start_date, @data_threshold
	END
END
------------------------------DATE AND TIME QUERIES------------------------------


DATEPART(datepart, date): Returns part, defined by abbrev. below, of the date
		year			yy, yyyy
		quarter			qq, q
		month			mm, m
		dayofyear		dy, y
		day				dd, d
		week			wk, ww
		weekday			dw, w
		hour			hh
		minute			mi, n
		second			ss, s
		millisecond		ms
		microsecond		mcs
		nanosecond		ns
		NOW()		









ADDDATE()								-- Adds dates
ADDTIME()								-- Adds time
CONVERT_TZ()							-- Converts from one timezone to another
CURDATE()								-- Returns the current date
CURRENT_DATE(), CURRENT_DATE			-- Synonyms for CURDATE()
CURRENT_TIME(), CURRENT_TIME			-- Synonyms for CURTIME()
CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP	-- Synonyms for NOW()
CURTIME()								-- Returns the current time
DATE_ADD()								-- Adds two dates
DATE_FORMAT()							-- Formats date as specified
DATE_SUB()								-- Subtracts two dates
DATE()								    -- Extracts the date part of a date or datetime expression
DATEDIFF()				                -- Subtracts two dates
DAY()					                -- Synonym for DAYOFMONTH()
DAYNAME()				                -- Returns the name of the weekday
DAYOFMONTH()			                -- Returns the day of the month (1-31)
DAYOFWEEK()				                -- Returns the weekday index of the argument
DAYOFYEAR()				                -- Returns the day of the year (1-366)
EXTRACT					                -- Extracts part of a date
FROM_DAYS()				                -- Converts a day number to a date
FROM_UNIXTIME()			                -- Formats date as a UNIX timestamp
HOUR()					                -- Extracts the hour
LAST_DAY				                -- Returns the last day of the month for the argument
LOCALTIME(), LOCALTIME	                -- Synonym for NOW()
LOCALTIMESTAMP, LOCALTIMESTAMP()	    -- Synonym for NOW()
MAKEDATE()			                    -- Creates a date from the year and day of year
MAKETIME			                    -- MAKETIME()
MICROSECOND()		                    -- Returns the microseconds from argument
MINUTE()			                    -- Returns the minute from the argument
MONTH()				                    -- Return the month from the date passed
MONTHNAME()			                    -- Returns the name of the month
NOW()				                    -- Returns the current date and time
PERIOD_ADD()		                    -- Adds a period to a year-month
PERIOD_DIFF()		                    -- Returns the number of months between periods
QUARTER()			                    -- Returns the quarter from a date argument
SEC_TO_TIME()		                    -- Converts seconds to 'HH:MM:SS' format
SECOND()			                    -- Returns the second (0-59)
STR_TO_DATE()		                    -- Converts a string to a date
SUBDATE()			                    -- When invoked with three arguments a synonym for DATE_SUB()
SUBTIME()			                    -- Subtracts times
SYSDATE()			                    -- Returns the time at which the function executes
TIME_FORMAT()		                    -- Formats as time
TIME_TO_SEC()		                    -- Returns the argument converted to seconds
TIME()				                    -- Extracts the time portion of the expression passed
TIMEDIFF()			                    -- Subtracts time
TIMESTAMP()			                    -- With a single argument, this function returns the date or datetime expression. 
										-- With two arguments, the sum of the arguments
TIMESTAMPADD()		                    -- Adds an interval to a datetime expression
TIMESTAMPDIFF()		                    -- Subtracts an interval from a datetime expression
TO_DAYS()			                    -- Returns the date argument converted to days
UNIX_TIMESTAMP()	                    -- Returns a UNIX timestamp
UTC_DATE()			                    -- Returns the current UTC date
UTC_TIME()			                    -- Returns the current UTC time
UTC_TIMESTAMP()		                    -- Returns the current UTC date and time
WEEK()				                    -- Returns the week number
WEEKDAY()			                    -- Returns the weekday index
WEEKOFYEAR()		                    -- Returns the calendar week of the date (1-53)
YEAR()				                    -- Returns the year
YEARWEEK()			                    -- Returns the year and week

------------------------------THE END------------------------------
