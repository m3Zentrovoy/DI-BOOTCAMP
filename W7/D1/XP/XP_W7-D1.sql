--🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
--------------------------------------------------------
-- DROP TABLE IF EXISTS df_employee;

-- CREATE TABLE df_employee AS
-- SELECT
--     s.employee_id || '_' || TO_CHAR(s.date, 'YYYY-MM-DD') AS id,
--     TO_CHAR(s.date, 'YYYY-MM') AS month_year,
--     s.employee_id,
--     s.employee_name,
--     e.gen_m_f AS gender,
--     e.age,
--     s.salary::numeric AS salary,
--     f.function_group,
--     s.comp_name AS company_name,
--     c.company_city,
--     c.company_state,
--     c.company_type,
--     c.const_site_category
-- FROM
--     salaries s
-- LEFT JOIN employees e ON s.employee_id = e.employee_code_emp
-- LEFT JOIN functions f ON s.func_code = f.function_code
-- LEFT JOIN companies c ON s.comp_name = c.company_name;

--------------------------------------------------------
--🌟 Exercise 2: Cleaning Data for Consistency and Quality
--------------------------------------------------------
-- SELECT * FROM df_employee

--2. Remove all unwanted spaces from all text columns using TRIM

-- UPDATE df_employee
-- SET
--     employee_name = TRIM(employee_name),
--     gender = TRIM(gender),
--     function_group = TRIM(function_group),
--     company_name = TRIM(company_name),
--     company_city = TRIM(company_city),
--     company_state = TRIM(company_state),
--     company_type = TRIM(company_type),
--     const_site_category = TRIM(const_site_category);

--3. Check for NULL values and empty values.

-- SELECT *
-- FROM df_employee
-- WHERE
--     id IS NULL
--     OR month_year IS NULL
--     OR employee_id IS NULL
--     OR employee_name IS NULL
--     OR gender IS NULL
--     OR age IS NULL
--     OR salary IS NULL
--     OR function_group IS NULL
--     OR company_name IS NULL
--     OR company_city IS NULL
--     OR company_state IS NULL
--     OR company_type IS NULL
--     OR const_site_category IS NULL;

--4. Delete rows of the detected missing values.

-- DELETE FROM df_employee
-- WHERE
--     id IS NULL
--  OR month_year IS NULL
--  OR employee_id IS NULL
--  OR employee_name IS NULL
--  OR gender IS NULL
--  OR age IS NULL
--  OR salary IS NULL
--  OR function_group IS NULL
--  OR company_name IS NULL
--  OR company_city IS NULL
--  OR company_state IS NULL
--  OR company_type IS NULL
--  OR const_site_category IS NULL;


--------------------------------------------------------
--🌟 Exercise 3 : Calculating Current Employee Counts by Company
--------------------------------------------------------

-- SELECT company_name, COUNT(DISTINCT employee_name) as Employee_Counts
-- FROM df_employee
-- GROUP BY company_name


--------------------------------------------------------
--🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
--------------------------------------------------------

--What is the total number of employees each city? Add a percentage column

-- SELECT
-- company_city,
-- COUNT(employee_name) as employee_counts,
-- ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percent_of_total
-- FROM df_employee
-- group by company_city

--What is the total number of employees each month?

-- SELECT
-- 	s.date,
-- 	COUNT(DISTINCT df.employee_name)	
-- FROM df_employee df
-- JOIN salaries s ON df.employee_id = s.employee_id
-- GROUP BY s.date
-- ORDER BY s.date


--What is the average number of employees each month?

-- SELECT
--     AVG(employees_per_month) AS avg_employees_per_month
-- FROM (
--     SELECT
--         month_year,
--         COUNT(DISTINCT employee_id) AS employees_per_month
--     FROM df_employee
--     GROUP BY month_year
-- ) AS monthly_counts;

-----------------------------------------------------------------
--🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
-----------------------------------------------------------------
--What is the minimum and maximum number of employees throughout all the months? In which months were they?

-- For each month, show the number of unique employees.

-- WITH monthly_counts AS (
--     SELECT
--         s.date AS month,
--         COUNT(DISTINCT df.employee_id) AS employees_per_month
--     FROM df_employee df
--     JOIN salaries s ON df.employee_id = s.employee_id
--     GROUP BY s.date
-- )
-- SELECT *
-- FROM monthly_counts
-- WHERE employees_per_month = (SELECT MIN(employees_per_month) FROM monthly_counts)
--    OR employees_per_month = (SELECT MAX(employees_per_month) FROM monthly_counts);




--What is the monthly average number of employees by function group?

-- SELECT
--     t.function_group,
--     ROUND(AVG(t.employee_count), 2) AS avg_employees_per_month
-- FROM (
--     SELECT
--         f.function_group,
--         TO_CHAR(TO_DATE(s.date::text, 'YYYY-DD-MM'), 'YYYY-MM') AS month_year,
--         COUNT(DISTINCT s.employee_id) AS employee_count
--     FROM
--         salaries s
--     LEFT JOIN functions f ON s.func_code = f.function_code
--     GROUP BY
--         f.function_group,
--         TO_CHAR(TO_DATE(s.date::text, 'YYYY-DD-MM'), 'YYYY-MM')
-- ) t
-- GROUP BY
--     t.function_group
-- ORDER BY
--     avg_employees_per_month DESC;



--What is the annual average salary?

SELECT
    EXTRACT(YEAR FROM date) AS year,
    ROUND(AVG(salary), 2) AS avg_salary
FROM
    salaries
GROUP BY 
    year
ORDER BY
    year;