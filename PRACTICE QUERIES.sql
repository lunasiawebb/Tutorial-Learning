-- TEMPORARY TABLE
CREATE TEMPORARY TABLE temp_table
( FIRST varchar(50),
LAST varchar(50),
favmovie varchar(100)
);

SELECT *
FROM temp_table;

INSERT INTO temp_table
VALUES ('Alex', 'MI', 'MOVIE');

SELECT * 
FROM employee_salary;

CREATE TEMPORARY TABLE salary50k
SELECT  *
FROM employee_salary 
WHERE salary > 50000
;

SELECT *
FROM salary50k;

-- STRING FUNCTIONS
-- LENGTH # of characters
SELECT LENGTH('skyfall');

SELECT first_name, LENGTH(first_name)
FROM employee_demographics
ORDER BY 2;

-- UPPER - make it all upper case
SELECT first_name, UPPER(first_name)
FROM employee_demographics;

-- TRIM rid of white spaces you can do LTRIM or RTRIM or both = TRIM
SELECT TRIM('       sky      ');

-- SUBSTRING LEFT takes certain # of characters from the left 
SELECT first_name, 
LEFT(first_name, 4), 
RIGHT(first_name, 4), 
SUBSTRING(first_name,3,2)
FROM employee_demographics;

-- REPLACE
SELECT first_name, REPLACE(first_name, 'a','z')
FROM employee_demographics;

SELECT LOCATE('x','Alexander');

SELECT first_name, LOCATE('An',first_name)
FROM employee_demographics;

-- CONCAT
SELECT first_name, last_name,
CONCAT(first_name, ' ',last_name) AS full_name
FROM employee_demographics;

-- SUBQUERIES 
-- Use 2nd select to filter choice 

-- select all in ed where emp id is also in dept 1
SELECT *
FROM employee_demographics
WHERE employee_id IN
		(SELECT employee_id
		FROM employee_salary
		WHERE dept_id = 1)
;

-- aggregate of all instead of individuals 
Select first_name, salary,
(SELECT AVG(salary)
FROM employee_salary)
FROM employee_salary;

-- double aggregation
Select AVG(MAX(age))
FROM
(SELECT gender,
AVG(age) AS avg_age,
MAX(age) AS max_age,
MIN(age) AS min_age,
COUNT (age)
FROM employee_demographics
GROUP BY gender) AS Agg_table
;

-- Stored Procedure
SELECT *
FROM employee_salary
WHERE salary >= 50000;

CREATE PROCEDURE large_salaries()
SELECT *
FROM employee_salary
WHERE salary >= 50000
;

-- delimiter used to put multiple queries in a procedure
DELIMITER  $$
CREATE PROCEDURE large_salaries2()
BEGIN
	SELECT *
	FROM employee_salary
	WHERE salary >= 50000;
	SELECT *
	FROM employee_salary
	WHERE salary >= 10000;
END $$
DELIMITER ;

CALL large_salaries();
CALL large_salaries2();

-- parameter
DROP PROCEDURE IF EXISTS large_salaries4;
DELIMITER $$
CREATE PROCEDURE large_salaries4(id INT)
BEGIN
	SELECT salary
	FROM employee_salary
    WHERE employee_id = id
	;
END $$
DELIMITER ;

CALL large_salaries4(1);

-- triggers and events
SELECT *
FROM employee_demographics;

SELECT *
FROM employee_salary;

DELIMITER $$
CREATE TRIGGER employee_insert
	AFTER INSERT ON employee_salary
    FOR EACH ROW 
BEGIN 
	INSERT INTO employee_demographics (employee_id, first_name, last_name)
    VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
END $$
DELIMITER ;

INSERT INTO employee_salary (employee_id, first_name, last_name, occupation, salary, dept_id)
VALUES(13, 'Lunasia', 'Webb', 'Informatician', 80000 , 1);

-- events
 SELECT *
 FROM employee_demographics; 
 
 DELIMITER $$
 CREATE EVENT delete_retirees
 ON SCHEDULE EVERY 30 SECOND
 DO
 BEGIN 
	DELETE
    FROM employee_demographics
    WHERE age >= 60;
END $$
DELIMITER ;

SHOW VARIABLES LIKE 'event%';
 
