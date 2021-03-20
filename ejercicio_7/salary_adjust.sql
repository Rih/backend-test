
/*
SELECT
    emp.first_name,
    emp.salary,
    cont.anual_adjustment Ajuste,
    cont.name Continente,
    cty.name Pais,
    emp.salary * (1 + cont.anual_adjustment/100) new_salary
    FROM employees emp
    INNER JOIN countries cty ON cty.id = emp.country_id
    INNER JOIN continents cont ON cty.continent_id = cont.id
*/

UPDATE employees
INNER JOIN countries cty ON cty.id = employees.country_id
INNER JOIN continents cont ON cty.continent_id = cont.id
SET salary = salary * (1 + cont.anual_adjustment/100)