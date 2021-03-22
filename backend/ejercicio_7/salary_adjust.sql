
-- QUERY TO CHECK IF UPDATE IS CORRECT
-- SELECT
--     emp.first_name,
--     emp.salary,
--     cont.anual_adjustment Ajuste,
--     cont.name Continente,
--     cty.name Pais,
--     emp.salary * (1 + cont.anual_adjustment/100.0) new_salary
--     FROM employees emp
--     INNER JOIN countries cty ON cty.id = emp.country_id
--     INNER JOIN continents cont ON cty.continent_id = cont.id
--     where emp.salary <= 5000


-- DML TESTED IN PostgreSQL ENGINE
UPDATE employees
SET salary = salary * (1 + continents.anual_adjustment/100.0)
FROM countries
INNER JOIN continents
    ON countries.continent_id = continents.id
WHERE
    employees.country_id = countries.id AND employees.salary <= 5000


