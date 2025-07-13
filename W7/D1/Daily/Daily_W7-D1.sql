--Identify and handle any missing value.
---------------------------------------------------------------

-- SELECT * FROM employees
-- WHERE employee_id IS NULL
-- OR employee_name IS NULL
-- OR salary IS NULL
-- OR hire_date IS NULL
-- OR department IS NULL

-- Replace NULL values in the department column with 'Unknown'

-- UPDATE employees
-- SET department = 'Unknown'
-- WHERE department IS NULL;

---------------------------------------------------------------
--Check for and eliminate any duplicate rows in the dataset.
---------------------------------------------------------------

-- SELECT
--   employee_name,
--   salary,
--   hire_date,
--   department,
--   COUNT(*)
-- FROM employees
-- GROUP BY employee_name, salary, hire_date, department
-- HAVING COUNT(*) > 1;

---------------------------------------------------------------
--Correct any structural issues, such as inconsistent naming conventions or formatting errors.
---------------------------------------------------------------

-- -- Change the data type of the hire_date column to DATE using type casting
-- ALTER TABLE employees
-- ALTER COLUMN hire_date TYPE DATE
-- USING hire_date::date;

-- -- Remove leading and trailing spaces from the employee_name column
-- UPDATE employees
-- SET employee_name = TRIM(employee_name);

-- -- Standardize department values: set 'HR' for all variants starting with 'hr'
-- UPDATE employees
-- SET department = 'HR'
-- WHERE department ILIKE 'hr%';

-- Capitalize the first letter of each word
-- UPDATE employees
-- SET employee_name = INITCAP(employee_name);


---------------------------------------------------------------
--Ensure all columns have appropriate data types (e.g. the hire_date column).
---------------------------------------------------------------

-- SELECT 
--     column_name, 
--     data_type
-- FROM 
--     information_schema.columns
-- WHERE 
--     table_name = 'employees';

---------------------------------------------------------------
--Detect and address any outliers that may skew the analysis.
---------------------------------------------------------------
-- Calculate the minimum, maximum, average, and standard deviation of employee salaries.
-- SELECT 
--     MIN(salary) AS min_salary,
--     MAX(salary) AS max_salary,
--     AVG(salary) AS avg_salary,
--     STDDEV(salary) AS stddev_salary
-- FROM employees;


---------------------------------------------------------------
--Standardize and normalize data where applicable to ensure consistency.
---------------------------------------------------------------
-- "Correct any structural issues, such as inconsistent naming conventions or formatting errors," 
-- has already been completed in the earlier section of the code.