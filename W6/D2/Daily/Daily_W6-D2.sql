
-- Q1. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- This will always return 0 rows.
-- Because NOT IN with NULL is always false.

-- Q2. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- This returns all rows except those where id = 5.
-- If there are no '5' in SecondTab, it returns all rows.

-- Q3. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- If there is at least one NULL in SecondTab,
-- this will always return 0 rows.
-- If there are no NULLs, it works as a normal NOT IN.

-- Q4. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- This returns all rows from FirstTab where id is not in SecondTab.
-- It ignores NULL values, so NOT IN works normally.	