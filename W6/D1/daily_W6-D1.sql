-- HOW TO CREATE A TABLE

-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(150) NOT NULL,
-- date_of_birth DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- )

-- HOW TO INSERT DATA INTO THE TABLE

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Meryl', 'Streep', '1949/06/22', 12)



-- -- EXERCISE 1 
-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('George', 'Clooney', '06/05/1961', 2),
-- ('Gal','Gadot', '1985/04/30', 2 ),
-- ('Brad', 'Pitt', '1963/12/18', 2);


-- TYPES OF SELECT QUERIES
-- SELECT last_name, number_oscars FROM actors

-- WHERE: CONDITION
-- SELECT last_name, number_oscars FROM actors WHERE number_oscars = 2
-- SELECT first_name, last_name, number_oscars FROM actors WHERE first_name = 'Matt'
-- AND last_name = 'Damon'

--LIKE = case sensitive
--ILIKE = not case sensitive
-- SELECT * FROM actors WHERE last_name ILIKE '%Mon%';
-- SELECT * FROM actors WHERE last_name ILIKE '%mon%';


-- LIMIT AND OFFSET:
-- SELECT * FROM actors LIMIT 3;

-- SELECT * FROM actors OFFSET 2;

-- SELECT * FROM actors WHERE number_oscars >= 5

-- ORDER BY
-- SELECT * FROM actors 


-- ALTER TABLE
-- UPDATE actors
-- SET date_of_birth = '08/10/1970'
-- WHERE
--     last_name = 'Damon';

-- DELETE FROM actors
-- WHERE first_name = 'Brad' AND last_name = 'Pitt';

-- TRUNCATE TABLE actors RESTART IDENTITY;


--1. Count how many actors are in the table.
-- SELECT COUNT(*) FROM actors


--2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
VALUES 
('Tom','Holand', NULL,NULL)

-- its gonna be wrong because - 

"-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(150) NOT NULL,
-- date_of_birth DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- )"


