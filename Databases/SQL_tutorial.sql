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

-- DATA TYPES:
    String      VARCHAR(1024)   -- Any characters with a maximum field length of 1024 characters
    Date/Time   TIMESTAMP       -- Stores year, month, day, hour, minute and second values as YYYY-MM-DD hh:mm:ss
    number      INTEGER
                DOUBLE PRECISION-- Numerical, with up to 17 significant digits decimal precision
                                    -- Does not support commas or currency symbols
                DECIMAL(10,5)   -- 10 digits, up to 2 decimal places
                NUMERIC(10,5)   -- 10 digits, up to 2 decimal places
    Boolean     BOOLEAN         -- Only TRUE or FALSE values

-- Columns can be cast to another type(within reason) with:
    CAST(expression AS [data type])
    column_name::[data type]
    CONVERT([data type], expression)

--------------------------Explore Database------------------------
    SHOW DATABASES
    SHOW TABLES
    DESCRIBE table_name

------------------------------Query Types------------------------------
------------------------------SELECT------------------------------
SELECT [ TOP x ] <fields>   -- STANDARD SELECT STRUCTURE
                            -- Can also select the top 50% "SELECT TOP 50 PERCENT"
FROM <Table1>
[ INNER JOIN <Table2>
    ON <fields> ]
[ WHERE <condition> ]       -- Filter records before the groups are made
[ GROUP BY <field>
[ HAVING <condition> ] ]    -- Filter records after the groups are made
[ ORDER BY <fields> ]
[ LIMIT y];

------------------------------CREATE------------------------------
CREATE DATABASE university_db

CREATE TABLE table_name                 -- Create a new table or view
(
    column_name1 data_type(size),       -- Create column of data-type and size

    p_id int 
        DEFAULT 77                      -- Set default values for column
        NULL                            -- Can have null values
        NOT NULL                        -- Cannot have null values
        CHECK (p_id > 0)                -- Must be > 0 
        IDENTITY(1, 1)                  -- Key automatically increase by one
        UNIQUE                          -- Unique
        PRIMARY KEY,                    -- Primary Key that and not null
  
    CONSTRAINT pk_person_id 
        PRIMARY KEY (p_id, last_name)   -- Add a named constraint, pk_Person_ID,
                                        --   such that list of columns forms Primary Key
    FOREIGN KEY (p_id) 
        REFERENCES Persons(p_id)        -- Ensure local key must exist as primary key on foreign table     
)

CREATE <UNIQUE> INDEX index_name          -- Create an index for a table (does not have to be unique)
    ON Table_name (last_name, first_name)
    # Combined column index is Faster for multiple AND connect terms in where clause
    # Slows down DML operations like INSERT, UPDATE and DELETE
    # Use indexes only on columns which are used to search the table frequently

CREATE OR REPLACE VIEW View_name AS     -- Create an on-the-fly view of a table
                                            -- (OR REPLACE will recreate if already view by that name)

------------------------------INSERT------------------------------
INSERT INTO Tbl_Players(first_name, last_name)  -- Add values in row to table
     VALUES (‘Douglas’, ‘Adams’)

------------------------------ALTER------------------------------
ALTER TABLE Table_name                  -- Change the structure of a table (fields)u
    ADD column_name data_type           -- Add a column of a certain data-type
    DROP COLUMN column_name             -- Delete column
    ALTER COLUMN column_name data_type  -- Change column data-type
    ALTER COLUMN city 
        SET DEFAULT 'SANDNES'           -- Add a default value for a column

    ALTER COLUMN city 
        DROP DEFAULT                    -- Delete default value for a column

    ADD PRIMARY KEY (p_id)              -- Add a Primary key
    DROP PRIMARY KEY                    -- Remove a Primary Key

    ADD CONSTRAINT pk_person_id 
        PRIMARY KEY (p_id, last_name)   -- Make Primary key from list of columns 
                                            -- (constraint named "pk_PersonID")

    ADD CONSTRAINT chk_person 
        CHECK (p_id > 0 AND 
               city = 'Sandnes')        -- Add constraints to multiple columns

    ADD CONSTRAINT uc_person_id 
        UNIQUE (p_id, last_name)        -- Add Uniqueness constraint to list of columns

    DROP CONSTRAINT uc_person_id        -- Delete a constraint

    ADD FOREIGN KEY (p_id)              -- Require that key column in table is in foreign table too
        REFERENCES Persons(p_id)

------------------------------UPDATE------------------------------
UPDATE Tbl_players              -- Change values in Table
    SET handicap = 17
    WHERE memb_no = 2

------------------------------DELETE------------------------------
DELETE FROM Tbl_Players         -- Delete rows from table
    WHERE memb_expire < NOW()

TRUNCATE TABLE Customers        -- Empty the  Table

-- TRUNCATE is faster than DELETE for a whole table

------------------------------DROP--------------------------------
-- A DROP TABLE statement cannot be rolled back
DROP DATABASE university_db

DROP TABLE IF EXISTS Table_name -- Delete table if it exists
                                    -- (Some SQL versions only)
DROP TABLE Table_name           -- Otherwise

IF OBJECT_ID('Respondent_Data', 'U') IS NOT NULL

DROP INDEX Table_Name.index_name-- Drop index from a table

DROP VIEW                       -- Drop a view

----------------COMPLETE SELECT SAMPLE STATEMENT------------------
USE [schema_name];                              -- Which Schema to use, otherwise it always has to precede the table name

SELECT TOP 100 + (5 * 2) / 2.5 , year, month,   -- Can use arithmetic operations (+, -, *, /) with columns BODMAS brackets
    a.*,                                        -- Select all columns from Table alias a
    name                    AS new_name,        -- Give column new name, can be used later in query
                                                -- Use AS "Title with Spaces" for spaces
    -- Numerical
    COUNT(artist)           AS num_artists,     -- Counts artist column NOT nulls
    SUM(earnings)           AS profit,          -- Sums column, treats nulls as 0
    AVG(group_members)      AS avg_band_size,   -- Find column average, completely ignores nulls (doesn't treat like zeros)
    MIN(year)               AS earliest_year,   -- Column minimum
                                                    -- Handles dates, numbers and strings
    MAX(albums_sold)        AS max_sold,        -- Column maximum
                                                    -- Handles dates, numbers and strings
    ABS(cost)               AS abs_cost,        -- Absolute Value
    STDEV(group_members)    AS std_dev_members, -- Standard Deviation
    VAR(group_members)      AS variance_members,-- Variance
    ROUND(price, 0)         AS round_price,     -- Round column to 0 decimals
    DISTINCT(month)         AS uniq_months,     -- DISTINCT returns unique entries in month column
                                                    -- DISTINCT(year, month) will return unique pairs
                                                    -- "SELECT DISTINCT * ..." will return unique rows
                                                    -- DISTINCT performs slowly
    -- Strings
    UPPER(stringy),                             -- Return string in uppercase
    LOWER(stringy,                              -- Return string in lowercase
    STRING_SPLIT('Lorem ipsum', ' ');           -- Split string by char

    -- Nulls
    COALESCE(option_1, option_2, ..., 0),       -- Returns first non null argument (here used to replace nulls with zero)
    IFNULL(units_on_order, 0),                  -- Returns 0 if UnitsOnOrder is NULL
                                                -- Same as NULLIF
                                                -- Avoid division by NULL 
                                                    -- SELECT IFNULL(dividend/divisor, 0)

    CASE

        ELSE  'We Do Not Have Records For This Customer'
        END AS 'result',

    CASE WHEN weight > 250                      -- IF THEN ELSE statement
            THEN 'over 250'                     
         WHEN weight > 200 
                AND weight <= 250 
            THEN '201-250'
         WHEN weight > 175 
                AND weight <= 200 
            THEN '176-200'
         WHEN EXISTS(SELECT 1
                     FROM Call_records
                     WHERE account = @accountnumber
                    )
            THEN 'We Have Records of this Customer'
         ELSE '175 or under'                    -- ELSE is optional
         END AS weight_group

-- FROM song_schema.song_data as artists
FROM songs_schema.songs songs a                 -- Can be given an alias, here just "a"
    JOIN artist_schema.artist earnings b
        ON songs.artist = earnings.artist
        AND companies.name = investments.company_name                   -- Joining on more than one key, even if unnecessary is much faster.
        AND acquisitions.company_permalink != '/company/1000memories'   -- Additional condition for merger 
                                                                        -- Evaluated before WHERE

/*
    FOR INNER JOIN - returns only overlap in data
        If multiple matches, all matches will be returned as separate rows
        If no matches no row is returned
        If two same named columns they will have the same resultant data
        Can be renamed as:
             SELECT players.school_name AS players_school_name,
                    teams.school_name   AS teams_school_name
               FROM benn.college_football_players players
                    JOIN benn.college_football_teams teams
                        ON teams.school_name = players.school_name

    FOR OUTER JOIN - Can return unmatched rows from either set (LEFT/RIGHT JOIN)
                     or FULL OUTER JOIN returns unmatched rows from both

    FOR FULL OUTER JOIN - Returns a left, inner and right join
*/

/*
    -- To exclude some rows where they appear in another table
        SELECT Table_1.* 
        FROM Table_1
            LEFT JOIN Table_2
                ON Table_1.id = Table_2.id
        WHERE Table_2.id IS NULL
        -- Can be used similarly to ONLY Take shared rows with IS NOT NULL

    SELECT *
    FROM Companies c
        LEFT JOIN Acquisitions a
            ON c.permalink = a.permalink

    In this join, companies data is either left alone or added to
    It is a CONVENTION to use LEFT JOIN over JOIN, not logically necessary
*/

WHERE month = 1                     -- =, !=, >, <, >=, and <=
                                    -- "!=" is the same as "<>"
                                    -- or month = 'January' in single quotes, operators now refer to alphabetic order
    AND 'day' LIKE '%day'           -- Case-sensitive
    OR 'day' ILIKE '%dAY'           -- Case-insensitive, "%"" is a multi-wildcard character
                                    -- 'day' LIKE 'Mo_day', "_" is a single wildcard character
    OR 'day' LIKE '[mtw]%day'       -- [charlist] Set range of characters to match e.g. [abc] or [a-c] or [0-9]
                                    -- [!charlist] Set range of characters to not match e.g. [!abc]

    AND 'artist' IN ('Taylor Swift', -- Can be expensive if the list is long.
                     'Ludacris',     --  Then do a join onto a sub_query table
                      1, 2, 3)       --  containing all these fields.
    AND year BETWEEN 1999 AND 2016  -- BETWEEN is inclusive of bounds
                                    -- Can use NOT BETWEEN to get outside range
                                    -- Dont use it for dates because "BETWEEN 2000-01-01 AND 2000-01-02"
                                    --  will get all the data on both 01-01 and 01-02
    AND band IS NOT NULL            -- band != NULL won't work(arithmetic on a str)
                                    -- Only with conditional statement
    OR band = 'Gotye'
    OR (band = 'MUSE' 
        AND 'album' = 'Absolution')

GROUP BY year, month                -- Creates only unique year, month rows with the remaining columns
                                        -- grouped into vectors which can be operated on
                                    -- Order doesn't matter
                                    -- GROUP BY 1,2 means group by the first two columns mentioned after SELECT; those created
                                    -- Cant use alias to order group etc
                                    -- Group functions can be nested to a depth of two

HAVING MAX(earnings) > 1000000      -- Like a where statement for which groups are selected APPLIED AFTER Grouping

ORDER BY year DESC,                 -- Ascending by default when no DESC
         artist                     -- Artist is second column to sort by
                                        
LIMIT 100                           -- Result only cut down to limit at end of operation(so doesn't affect results)

--/////////////////////////////END OF SAMPLE SELECT STATEMENT////////////////////////////////////

------------------------------GROUPING------------------------------
/*
    For when grouping by different conditions
    Create the groups with a multiple case then statement
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
    FROM Football_players
    GROUP BY 1

    -- Include aggregate value without grouping 
    SELECT  SUM(Cost) OVER (PARTITION BY CustomerNo) AS Cost
            , OrderNum
            , CustomerNo
    FROM Orders
    --> 
        +------+----------+------------+
        | Cost | OrderNum | CustomerNo |
        +------+----------+------------+
        | 8.00 |    345   |     1      |
        | 8.00 |    346   |     1      |
        | 8.00 |    347   |     1      |
        | 2.00 |    348   |     2      |
        +------+----------+------------+

------------------------------SETS------------------------------
-- Must have same number of columns, and data types
-- Column names don't have to be the same
    SELECT *
    FROM Investments_part1
    UNION                   -- Removes rows from Table 2 identical to any in Table 1
                            -- UNION ALL joins all the rows regardless
    SELECT *
    FROM Investments_part2


    SELECT *                -- Remove from 1st set items in the 2nd
    FROM Employee
    MINUS
    SELECT * 
    FROM Employee 
    WHERE id > 2

    SELECT *                -- Keep common items only
    FROM Employee 
    WHERE id IN (2, 3, 5)
    INTERSECT
    SELECT * 
    FROM Employee 
    WHERE id IN (1, 2, 4, 5)

------------------------------STRING_EXPRESSIONS------------------------------
LEN(string_var)                         -- Return the length of the string
                                        --   not including trailing spaces
LEFT(string_var, index)                 -- Take from char 1 to index
MID(string_var)                         -- Take mid char
RIGHT(string_var, index)                -- Take from char 1 to index
LENGTH('stringy')                       -- Get length of string
REPLACE (str1, str2, str3)              -- In str1, find where str2 occurs, and replace it with str3
TRIM( [ <LOCATION> [remstr] FROM ] str) -- <LOCATION> can be either LEADING, TRAILING, or BOTH
                                        -- If <remstr> pattern is not given white spaces are removed
CONCAT(str1, str2, str3, ...)           -- Concatenate all strings
    'What' || ' the' || '....?'
SUBSTRING(stringy, index_1, index_2)    -- Take substring between index_1 and index_2
CHARINDEX('-', stringy)                 -- Find Position of character in string

------------------------------MATHEMATICAL_EXPRESSIONS------------------------
ABS(x)        -- Absolute value of x
SIGN(x)       -- Sign of input x as -1, 0, or 1
MOD(x, y)     -- (same as x%y)
FLOOR(x)      -- Largest integer value that is less than or equal to x
CEIL(x)       -- Smallest integer value that is greater than or equal to x
POWER(x, y)   -- x raised to the power of y
ROUND(x, d=0) -- x rounded to the d number of decimal
SQRT(x)       -- Square-root value of x

------------------------------LOGICAL EXPRESSIONS-----------------------------
IS NULL
IS NOT NULL
IIF(handicap <= 15, ‘Good’, ‘Bad’)

-- Cannot compare nulls and values
    +---------------+--------+
    |  Comparison   | Result |
    +---------------+--------+
    | 1 = 1         |  TRUE  |
    | 1 = 0         |  FALSE |
    | 1 = NULL      |  NULL  |
    | 1 != NULL     |  NULL  |
    | 1 IS NULL     |  FALSE |
    | 1 IS NOT NULL |  TRUE  |
    +---------------+--------+

------------------------------PIVOTING-----------------------------------------
-- WHERE Year is categorical column, and sales_amount is to be aggregated
-- Static

SELECT country, [2005], [2006], [2007], [2008], [2009], [2010]
FROM Table
    PIVOT
    (
        SUM(sales_amount)
        FOR [year] IN ([2005], [2006], [2007], [2008], [2009], [2010])
    ) AS P

-- Dynamic

    -- Declare necessary variables
    DECLARE @SQLQuery       AS NVARCHAR(MAX)
    DECLARE @pivot_columns  AS NVARCHAR(MAX)

    -- Get unique values of pivot column
    SELECT @pivot_columns = COALESCE(@pivot_columns + ',', '') + QUOTENAME(year)
    FROM (SELECT DISTINCT year
          FROM Table) AS PivotExample

    -- Create the dynamic query with all the values for
    -- pivot column at runtime
    SET @SQLQuery =
        N'SELECT country, ' + @pivot_columns + '
        FROM Table
        PIVOT(SUM(sales_amount)
            FOR year IN (' + @pivot_columns + ')) AS P'

    -- Execute dynamic query
    EXEC sp_executesql @SQLQuery

-----------------------------------Dynamic SQL ---------------------------
BEGIN
    -- Declaring variables
    DECLARE @Source_table   varchar(max)
           ,@start_date     DATETIME
           ,@data_threshold numeric

    SET @Source_table   = '[db_ucg].[dbo].[source_table]'
    SET @Table_name     = '[db_ucg].[dbo].[target_table]'
    SET @start_date     = '2016-02-01 00:00:00.000'
    SET @data_threshold = SELECT 1024 / 10      -- CAN USE SQL HERE

    BEGIN
        -- Make command String
        SET @cmd = 'SELECT * ' ||
        '           INTO ' + @Table_name +
                   ' FROM ' + @Source_table

        -- Execute common string with necessary input
            -- "string of parameters", parameter_1, parameter_2, ...
        exec sp_executesql @cmd,N'  @table_name nvarchar(50), 
                                    @start_date DATETIME, 
                                    @data_threshold numeric',
                                        @Table_name, 
                                        @start_date, 
                                        @data_threshold
    END
END

-----------------------------------Performance Issues ---------------------------

    -- EXPLAIN / EXPLAIN PLAN / EXPLAIN QUERY PLAN
        EXPLAIN <query>
            ==> (cost=0.00..18584.82 rows=1025082 width=36)

        EXPLAIN ANALYSE <query>
            ==> (cost=0.00..18334.00 rows=1000000 width=37)
                (actual time=0.015..1207.019 rows=1000000 loops=1)
                Total runtime: 2320.146 ms

    -- Select only columns you need

    -- Aggregate BEFORE joining tables where possible

    -- Join on multiple fields (if they're indexed) even if only one is necessary

    -- UNION ALL is faster than UNION

    -- Rather use exist which will stop after finding the 1st item
        SELECT column
        FROM Table
        WHERE COUNT(column) > 0

    -- Avoid sub-queries dependent on outer loop
        -- Rather do joins
        SELECT *
        FROM Users
        WHERE id IN (SELECT id
                     FROM Fines
                     WHERE Users.id = Fines.id)

        -- Otherwise sub-queries can actually be much faster

    -- Use UNION over OR in this case
        * Worse to read however
            SELECT *
            FROM Users
            WHERE id = 'value1'
                OR birthplace = 'value2'

            =>  SELECT *
                FROM Users
                WHERE id = 'value1'
                UNION
                SELECT *
                FROM Users
                WHERE birthplace = 'value2'

    -- These scale rapidly:
        ORDER BY
        DISTINCT
        LIKE --with % or _

    -- EXISTS preferred over IN
        SELECT *
        FROM Products
        WHERE product_id IN (SELECT product_id
                             FROM Ordered_items)

        =>  SELECT *
            FROM Products p
            WHERE EXISTS (SELECT *
                          FROM Ordered_items o
                          WHERE o.product_id = p.product_id)

    -- Avoid unnecessary computation in WHERE clauses
       eg. WHERE height + 1 = 10

    -- Favour small data types over large data types
       Data conversions cost time

    -- Use IN over OR where possible
        SELECT *
        FROM Users
        WHERE  id = 1
            OR id = 2
            OR id = 3

        =>  SELECT *
            FROM Users
            WHERE id IN (1, 2, 3)

    -- Index the database

    -- Don't do in multiple selects what can be done in one
        SELECT <something> 
        FROM Users
        UNION
        SELECT <something_else> 
        FROM Users

    -- Favour using >, <, <=, and >= over NOT when possible

    -- Favour between over < and > range
        SELECT *
        FROM Table
        WHERE year > 1
            AND year < 3

        ==>     SELECT *
                FROM Table
                WHERE year BETWEEN 1 AND 3

    -- Order Tables in joins
        SELECT *
        FROM <Small_Table> s
             JOIN
             <Large_Table> l
                 ON s.id = l.id

    -- Favour WHERE over HAVING when aggregation is unnecessary to apply condition
        -- It will be applied earlier in the process and save time

------------------------------DATE AND TIME QUERIES------------------------------
-- Current Time
NOW()                                   -- Returns the current date and time
CURTIME()/CURRENT_TIME()                -- Returns the current time
CURDATE()/CURRENT_DATE()                -- Returns the current date
CURRENT_TIMESTAMP()                     -- Synonym for NOW()
LOCALTIME()/LOCALTIMESTAMP()            -- Synonym for NOW()
SYSDATE()                               -- Returns the time at which the function executes
UTC_DATE()/ UTC_TIME()/UTC_TIMESTAMP()  -- Returns the current UTC date

-- Date Algebra
DATEDIFF()      -- Subtracts two dates
PERIOD_ADD()    -- Adds a period to a year-month
PERIOD_DIFF()   -- Returns the number of months between periods
TIMESTAMPADD()  -- Adds an interval to a datetime expression
TIMESTAMPDIFF() -- Subtracts an interval from a datetime expression
ADDDATE()       -- Adds dates
ADDTIME()       -- Adds time
DATE_ADD()      -- Adds two dates
DATE_SUB()      -- Subtracts two dates
SUBTIME()       -- Subtracts times
TIMESTAMP()     -- With a single argument, this function returns the date or datetime expression
                     -- With two arguments, the sum of the arguments

-- Time periods
MICROSECOND()               -- Returns the microseconds from argument
SECOND()                    -- Returns the second (0-59)
MINUTE()                    -- Returns the minute from the argument
HOUR()                      -- Returns the hour
DAY()                       -- Returns the day of the month (1-31)
    DAYNAME()               -- Returns the name of the weekday
    WEEKDAY()               -- Returns the weekday index
    DAYOFMONTH()            -- Synonym for DAY()
    DAYOFWEEK()             -- Returns the weekday index of the argument
    DAYOFYEAR()             -- Returns the day of the year (1-366)
WEEK()                      -- Returns the week number
    WEEKOFYEAR()            -- Returns the calendar week of the date (1-53)
    YEARWEEK()              -- Returns the year and week
MONTH()                     -- Returns the month from the date passed
    MONTHNAME()             -- Returns the name of the month
    LAST_DAY                -- Returns the last day of the month for the argument
QUARTER()                   -- Returns the quarter from a date argument
YEAR()                      -- Returns the year

DATENAME(DAY, datetime)     -- Tuesday

-- Extract
DATE()                      -- Extracts the date part of a date or datetime expression
EXTRACT()                   -- Extracts part of a date
DATEPART(datepart, date)    -- Returns part, defined by abbreviation below, of the date
    +-------------+---------+
    |   Datepart  |   code  |
    +-------------+---------+
    | year        | yy, yyyy|
    | quarter     | qq, q   |
    | month       | mm, m   |
    | dayofyear   | dy, y   |
    | day         | dd, d   |
    | week        | wk, ww  |
    | weekday     | dw, w   |
    | hour        | hh      |
    | minute      | mi, n   |
    | second      | ss, s   |
    | millisecond | ms      |
    | microsecond | mcs     |
    | nanosecond  | ns      |
    +-------------+---------+

-- Formatting
DATE_FORMAT()   -- Formats date as specified
FROM_DAYS()     -- Converts a day number to a date
FROM_UNIXTIME() -- Formats date as a UNIX timestamp
SEC_TO_TIME()   -- Converts seconds to 'HH:MM:SS' format
STR_TO_DATE()   -- Converts a string to a date
TIME_FORMAT()   -- Formats as time
TIME_TO_SEC()   -- Returns the argument converted to seconds
TO_DAYS()       -- Returns the date argument converted to days
UNIX_TIMESTAMP()-- Returns a UNIX timestamp
CONVERT_TZ()    -- Converts from one timezone to another
MAKEDATE()      -- Creates a date from the year and day of year

                    ------------------------------THE END------------------------------


                    --------------------------- TO DO ITEMS ---------------------------

-- PERMISSIONS
    GRANT privilege_name                    -- System privileges - CREATE, ALTER, or DROP database objects
                                            -- Object privileges - EXECUTE, SELECT, INSERT, UPDATE or DELETE data
        ON object_name                      -- Object_name - TABLE, VIEW, STORED PROC and SEQUENCE
        TO {user_name | PUBLIC | role_name} -- PUBLIC is used to grant access rights to all users
        [WITH GRANT OPTION]                 -- Allows a user to grant access rights to other users

    REVOKE privilege_name                   -- You cannot REVOKE privileges not initially granted by you
        ON object_name                      -- Revoked only if everyone who granted the permission revokes it
        FROM {user_name | PUBLIC | role_name} 

    -- ROLES are a set of privileges grouped together
        CREATE ROLE role_name 
            [IDENTIFIED BY password]

        GRANT CREATE TABLE 
            TO role_name

        GRANT role_name 
            TO user1

        DROP ROLE role_name

-- Processes:
SHOW PROCESSLIST
KILL <p_id>

-- See column names available
 SHOW COLUMNS FROM table_name

-- Transactions:
  BEGIN TRY
    BEGIN TRANSACTION
      <sql_script_here>
    COMMIT TRANSACTION
  END TRY
  BEGIN CATCH
    ROLLBACK TRANSACTION
  END CATCH

    -- To set automatic rollbacks on transactions:
        SET XACT_ABORT ON

--- Procedure function
-- Define a name and parameters
  CREATE PROCEDURE Northwind.getEmployee
    @LastName nvarchar(50),
    @FirstName nvarchar(50)
  AS
    -- Define the query to be run
    SELECT FirstName, LastName, Department
    FROM Northwind.vEmployeeDepartment
    WHERE FirstName = @FirstName
      AND LastName = @LastName
      AND EndDate IS NULL;

  --Calling the procedure:
    EXECUTE Northwind.getEmployee N'Ackerman', N'Pilar';

-- ANY and ALL
    -- Simple way to evaluate an inter-table condition without doing a join
    -- Find Items that are banned
        SELECT ProductName
        FROM Products
        WHERE ProductID = ANY (SELECT id 
                               FROM export_items 
                               WHERE is_banned = TRUE);

    --Alternatively:
        SELECT d.ProductName
        FROM Products p
        WHERE EXISTS (SELECT 'X' 
                      FROM banned_items b 
                      WHERE b.ProductName = p.ProductName)

    -- Find all legal items
        SELECT ProductName
        FROM Products
        WHERE ProductID != ALL (SELECT id 
                                FROM export_items 
                                WHERE is_banned = TRUE);

-- SELECT nth highest
    SELECT TOP (1) salary 
    FROM
        (SELECT DISTINCT TOP (10) salary
         FROM Employee
         ORDER BY salary DESC)
    ORDER BY salary

-- The MERGE statement allows conditional update or insertion of data into a database table
    --It performs an UPDATE if the rows exists, or an INSERT if the row does not exist

-- SQL INJECTION
    print("With Hack: \n")
    Name = "Robert'; DROP TABLE Students; --"
    print("SELECT * 
           FROM Students 
           WHERE name = '%s'" % name)

-- Dividing ints to make float
    SELECT 2 / 3
        -> 0

    SELECT 2 * 1.0 / 3
        -> 0.666666

    SELECT AVG(numbers) 
    FROM Table_name
        -> 2.0

    SELECT AVG(numbers * 1.0) 
    FROM Table_name
        -> 1.8


# TODO:
-- Time complexities 
    http://www.dalibo.org/_media/understanding_explain.pdf

    SELECT * FROM <>        O(N)
    COUNT()                 O(N)
    WHERE on non-indexed    O(N)
    WHERE on indexed        O(log(N))

    MERGE JOIN
    +-------------+--------------+-------------------+
    |  A (size M) |  B (size N)  |  Time Complexity  | 
    +-------------+--------------+-------------------+
    |      X      |      X       |       M + N       | 
    |             |      X       |   M*log(M) + N    |
    |      X      |              |    M + N*log(N)   |
    |             |              |M*log(M) + N*log(N)|
    +-------------+--------------+-------------------+

    NESTED JOIN generally O(MN)

    SELECT *
    FROM item, author 
    WHERE item.i_a_id = author.a_id 
    --O(Nlog(N)) < between < O(N^2) depending on indicies

-- 
    SELECT * 
    FROM Table
    WHERE 1=1
        AND column_name = 'James'
        AND column_surname = 'Jones'
    -- Easy to comment out first 'real' criteria
    -- Easy to reorder
    
-- COUNT (DISTINCT column-name)

-- This will return only record (n + 1) to (n + 1 + m). See example below.
   SELECT *
   FROM table
   OFFSET n ROWS
   FETCH NEXT m ROWS ONLY

-- Select random rows: (needs checking)
  -- SELECT 500 ROWS (or less)
  -- if you use just TABLESAMPLE it will return 1000/n_total rows rounded
  -- REPEATABLE sets the seed used when randomly sampling rows
  SELECT TOP(500) *
  FROM Orders TABLESAMPLE(1000 ROWS ) REPEATABLE (55)


--- NTiles:
  -- Setup data:
  DECLARE @values TABLE (Id INT IDENTITY(1,1) PRIMARY KEY, [VALUE ] FLOAT , ExamId INT)
  INSERT INTO @values ([VALUE], ExamId) VALUES
  (65, 1), (40, 1), (99, 1), (100, 1), (90, 1), -- Exam 1 Scores
  (91, 2), (88, 2), (83, 2), (91, 2), (78, 2), (67, 2), (77, 2) -- Exam 2 Scores

  -- Separate into four buckets per exam:
  SELECT ExamId,
  ntile(4) over (partition BY ExamId ORDER BY [VALUE ] DESC) AS Quartile,
  VALUE, Id
  FROM @values
  ORDER BY ExamId, Quartile


-- Convert Dates:
CONVERT(VARCHAR(30), GETDATE(), @convert_code)
  @convert_code   Result
  100             "Jul 21 2016 7:56AM"
  101             "07/21/2016"
  102             "2016.07.21"
  103             "21/07/2016"
  104             "21.07.2016"
  105             "21-07-2016"
  106             "21 Jul 2016"
  107             "Jul 21, 2016"
  108             "07:57:05"
  109             "Jul 21 2016 7:57:45:707AM"
  110             "07-21-2016"
  111             "2016/07/21"
  112             "20160721"
  113             "21 Jul 2016 07:57:59:553"
  114             "07:57:59:553"
  120             "2016-07-21 07:57:59"
  121             "2016-07-21 07:57:59.553"
  126             "2016-07-21T07:58:34.340"
  127             "2016-07-21T07:58:34.340"
  130             "16 ???? 1437 7:58:34:340AM"
  131             "16/10/1437 7:58:34:340AM"


--Format
DECLARE @Date DATETIME = '2016-09-05 00:01:02.333'
FORMAT(@Date, N'dddd, MMMM dd, yyyy hh:mm:ss tt')
  Argument Output
  yyyy      2016
  yy        16
  MMMM      September
  MM        09
  M         9
  dddd      Monday
  ddd       Mon
  dd        05
  d         5
  HH        00
  H         0
  hh        12
  h         12
  mm        01
  m         1
  ss        02
  s         2
  tt        AM
  t         A
  fff       333
  ff        33
  f         3

-- DATEADD
  DECLARE @now DATETIME2 = GETDATE();
  SELECT @now;                          -- 2016-07-21 14:39:46.4170000
  SELECT DATEADD(YEAR, 1, @now)         -- 2017-07-21 14:39:46.4170000
  SELECT DATEADD(QUARTER, 1, @now)      -- 2016-10-21 14:39:46.4170000
  SELECT DATEADD(WEEK, 1, @now)         -- 2016-07-28 14:39:46.4170000
  SELECT DATEADD(DAY, 1, @now)          -- 2016-07-22 14:39:46.4170000
  SELECT DATEADD(HOUR, 1, @now)         -- 2016-07-21 15:39:46.4170000
  SELECT DATEADD(MINUTE, 1, @now)       -- 2016-07-21 14:40:46.4170000
  SELECT DATEADD(SECOND, 1, @now)       -- 2016-07-21 14:39:47.4170000
  SELECT DATEADD(MILLISECOND, 1, @now)  -- 2016-07-21 14:39:46.4180000

--eg to check the age today of someone born on 1/1/2000
  SELECT dbo.Calc_Age('2000-01-01', Getdate())


-- End of Month:
    SELECT EOMONTH('2016-07-21')      -- 2016-07-31
    SELECT EOMONTH('2016-07-21', 4)   -- 2016-11-30
    SELECT EOMONTH('2016-07-21', -5)  -- 2016-02-29


-- Time differences:
  DECLARE @now DATETIME2 = GETDATE();
  DECLARE @oneYearAgo DATETIME2 = DATEADD(YEAR, -1, @now);
  SELECT @now                                   --2016-07-21 14:49:50.9800000
  SELECT @oneYearAgo                            --2015-07-21 14:49:50.9800000
  SELECT DATEDIFF(YEAR, @oneYearAgo, @now)      --1
  SELECT DATEDIFF(QUARTER, @oneYearAgo, @now)   --4
  SELECT DATEDIFF(WEEK, @oneYearAgo, @now)      --52
  SELECT DATEDIFF(DAY, @oneYearAgo, @now)       --366
  SELECT DATEDIFF(HOUR, @oneYearAgo, @now)      --8784
  SELECT DATEDIFF(MINUTE, @oneYearAgo, @now)    --527040
  SELECT DATEDIFF(SECOND, @oneYearAgo, @now)    --31622400


-- Create a function:
  CREATE FUNCTION [dbo].[Calc_Age]
    (
    @DOB datetime , @calcDate datetime
    )
    RETURNS int
    AS
    BEGIN
      DECLARE @age INT
      IF (@calcDate < @DOB)
      RETURN -1

      -- If a DOB is supplied after the comparison date, then return -1
      SELECT @age = YEAR(@calcDate) - YEAR(@DOB) +
                  CASE
                    WHEN DATEADD(year, YEAR(@calcDate) - YEAR(@DOB),@DOB) > @calcDate
                      THEN -1
                    ELSE 0
                  END
      RETURN @age
    END


-- read from a table without locking it (beware a table changing underneath you)
  SELECT *
  FROM TableName
  WITH (nolock)


-- create index to optimise select
  CREATE INDEX ix_scoreboard_score
  ON scoreboard (score DESC);

  -- When you execute the query
      SELECT *
      FROM scoreboard
      ORDER BY score DESC;

-- custom ordering scheme:
    -- order by department, city
    -- but department is custom sorted
  SELECT *
  FROM DEPT
  ORDER BY
    CASE DEPARTMENT
      WHEN 'MARKETING'  THEN 1
      WHEN 'SALES'      THEN 2
      WHEN 'RESEARCH'   THEN 3
      WHEN 'INNOVATION' THEN 4
      ELSE 5
    END,
    CITY

-- Triggers:
  CREATE TRIGGER MyTrigger
  ON MyTable
  AFTER INSERT  -- DELETE / UPDATE ...
  AS
  BEGIN
  -- insert audit record to MyAudit table
      INSERT INTO MyAudit(MyTableId, User)
      (SELECT MyTableId, CURRENT_USER
       FROM inserted)
  END

--SYNONYMS
  CREATE SYNONYM EmployeeData
  FOR MyDatabase.dbo.Employees

-- Order of processing
  /*(8)*/   SELECT /*9*/ DISTINCT /*11*/ TOP
  /*(1)*/   FROM
  /*(3)*/   JOIN
  /*(2)*/   ON
  /*(4)*/   WHERE
  /*(5)*/   GROUP BY
  /*(6)*/   WITH
  /*(7)*/   HAVING
  /*(10)*/  ORDER BY
  /*(11)*/  LIMIT


-- TO_CSV
    COPY (SELECT * FROM example_table) TO 'csv_name.csv' DELIMITER ',' CSV; -- Need admin rights
    --  else
    \copy (SELECT * FROM example_table) TO 'csv_name.csv' with csv


-- Row Numbering:
    SELECT Product_Category,
      Shipping_Address,
      Shipping_Cost,
      ROW_NUMBER() OVER
                  (PARTITION BY Product_Category,
                                Shipping_Address
                   ORDER BY Shipping_Cost DESC) as RowNumber,
      RANK() OVER
            (PARTITION BY Product_Category,
                          Shipping_Address
             ORDER BY Shipping_Cost DESC) as RankValues,
      DENSE_RANK() OVER
                  (PARTITION BY Product_Category,
                                Shipping_Address
                   ORDER BY Shipping_Cost DESC) as DenseRankValues
    FROM Dummy_Sales_Data_v1
    WHERE Product_Category IS NOT NULL
    AND Shipping_Address IN ('Germany','India')
    AND Status IN ('Delivered')

-- ROW_NUMBER - as in the name
-- RANK
    -- Given a number by the ordering, a tie is handled such that numbers can be skipped
1
1
3
4
5
-- DENSE_RANK
    -- When there is a tie, no number will be skipped:
1
1
2
3
-- TODO

On_DELETE_CASCADE foreign keys


-- Rebuilding index:
ALTER INDEX ix_cars_employee_id ON Cars REBUILD;

-- Using regex:
SELECT 'bedded' REGEXP '[a-f]' -- returns True

-- A stored view that is updated every so often - useful if slow to compute:
Materialized views

-- Good resource:
https://goalkicker.com/SQLBook/