### Backend Test: Desafío Envíame

El siguiente desafío, busca conocer más respecto a tus habilidades técnicas para abordar y solucionar diferentes problemas. El desafío consta de 7 etapas, las cuales, evaluaremos de manera independiente.

**Asegurate de dejar tu trabajo en un repositorio de github y al finalizar tu tarea nos compartes el repositorio donde deben incluirse todas las instrucciones para que podamos ejecutar tu trabajo de manera local.**

#### Importante: ####
**Los lenguajes a utilizar pueden ser: php, python, node.js**

En caso de preguntas dirigete a: *tech-test@enviame.io*, usando el asunto [Backend-Test]

### Ejercicio 1: Docker

Configura un ambiente en docker que permita ejecutar un entorno web con el stack a tu elección. 
El contenedor de la base de datos debe ser diferente al que contenga tu aplicación, ej: Contenedor 1: Nginx, Contenedor 2: Mysql (composición de servicios docker)

Solucion:
#### Prerequisitos: docker 19.03.2 o superior, docker-compose 1.24.1 o superior
* Ejecutar lo siguiente para construir servidores:
    1. `docker-compose build` o bien `sh bin/build-servers.sh` 
    2. Para iniciar: `docker-compose up -d` o bien `sh bin/start-dev-server.sh`
* Ejecutar lo siguiente para configurar nginx:
    1. `docker exec -it $(docker-compose ps -q web) bash`  o bien `sh bin/enter-web-server.sh`    
    2. `ln -s /nginx/app_back /etc/nginx/sites-enabled/app_back`
    
### Ejercicio 2: API REST + CRUD

Dentro del ambiente dockerizado desarrolla una API Rest, con el stack de tu preferencia, que implemente un CRUD de una entidad tipo 'empresa'. Preocupate de incluir un script que genere N registros con datos "fake" (utilizando una librería faker).

### Ejercicio 3: Análisis + Desarrollo 

Crea un script en el lenguaje de tu elección y encuentre la(s) cadena de texto que es(son) igual al revés en el siguiente texto:

`afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood`

### Ejercicio 4: Consumo API Envíame para la creación de un envío
Desarrolla una función o script que consuma la API Envíame para la creación de un Envío y almacene la respuesta en algún medio de almacenamiento permanente.
Documentación (Postman) del endpoint a usar: [Colección Postman](https://github.com/enviame/backend-test/blob/main/Backend-test.postman_collection.json)

### Ejercicio 5: Análisis + Desarrollo
La serie de Fibonacci se construye utilizando la siguiente relación de recurrencia: `Fn = Fn1 + Fn2, donde F1 = 1 y F2 = 1`. Por ende, los primeros doce términos de esta serie son: `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144`

Ahora, consideremos los divisores de estos términos:

```text
1 = 1
1 = 1
2 = 1, 2
3 = 1, 3
5  = 1, 5
8 = 1, 2, 4, 8
13 = 1, 13
21 = 1, 3, 7, 21
34 = 1, 2, 17, 34
55 = 1, 5, 11, 55
89 = 1, 89
144 = 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144
```

Como se puede ver, 144 es el primer número de la serie de Fibonacci que tiene más de 10 divisores (de hecho tiene 15).
Crea un script en tu lenguaje favorito que obtenga el primer número de Fibonacci que tiene más de 1000 divisores.


### Ejercicio 6: Análisis + Desarrollo Aplicado a Negocio
Desarrolla una función o procedimiento que estime el tiempo de entrega de la entrega de una compra online (en días), en función de la distancia que existe entre una dirección de origen y destino.

Suponga que los envíos siempre se despachan desde el mismo origen.

Para la determinación de la distancia entre el origen y destino genere números aleatorios entre 0 km y 2.000 km
Asuma que el tiempo de despacho está determinado por una sucesión numérica, donde cada N término se relaciona con un incremento en un rango de distancia entre la dirección de origen y de destino como se muesta a continuación.

* Rango 1. Menos de 100 km, se entregan el mismo día (Día cero) 
* Rango 2. Menos de 200 km, se entregan al día siguiente (Día uno)
* Rango 3. Menos de 300 km, se entregan al día siguiente (Día uno)
* Rango 4. Menos de 400 km, se entregan al día subsiguiente (Día dos)
* Rango 5. Menos de 500 km, se entregan al tercer día (Día tres)
...
* Rango n. Menos de n km, Los días de entrega se calculan como la suma de los días de entrega de los rangos n–1 y n-2

### Ejercicio 7: SQL
-- Actualizar los sueldos de los empleados que ganen $5000 o menos, de acuerdo al reajuste anual del continente al que pertenecen.

CREATE TABLE public."countries"(
  id  int PRIMARY KEY,
  continent_id int NOT NULL,
  name varchar(25) NOT NULL
);

CREATE TABLE public."continents"(
  id  int PRIMARY KEY,
  name varchar(25) NOT NULL,
  anual_adjustment int NOT NULL
);

CREATE TABLE public."employees"(
  id  int PRIMARY KEY,
  country_id int NOT NULL,
  first_name varchar(25) NOT NULL,
  last_name varchar(25) NOT NULL,
  salary int NOT NULL
);

insert into continents values (6, 'América', 4);
insert into continents values (2, 'Europa', 5);
insert into continents values (3, 'Asia', 6);
insert into continents values (4, 'Oceanía', 6);
insert into continents values (5, 'Africa', 5);

insert into countries (id, continent_id, name) values (1, 1, 'Chile');
insert into countries (id, continent_id, name) values (2, 1, 'Argentina');
insert into countries (id, continent_id, name) values (3, 1, 'Canadá');
insert into countries (id, continent_id, name) values (4, 1, 'Colombia');
insert into countries (id, continent_id, name) values (5, 2, 'Alemania');
insert into countries (id, continent_id, name) values (6, 2, 'Francia');
insert into countries (id, continent_id, name) values (7, 2, 'España');
insert into countries (id, continent_id, name) values (8, 2, 'Grecia');
insert into countries (id, continent_id, name) values (9, 3, 'India');
insert into countries (id, continent_id, name) values (10, 3, 'Japón');
insert into countries (id, continent_id, name) values (11, 3, 'Corea del Sur');
insert into countries (id, continent_id, name) values (12, 4, 'Australia');

insert into employees values (1, 1, 'Pedro', 'Rojas', 2000);
insert into employees values (2, 2, 'Luciano', 'Alessandri', 2100);
insert into employees values (3, 3, 'John', 'Carter', 3050);
insert into employees values (4, 4, 'Alejandra', 'Benavides', 2150);
insert into employees values (5, 5, 'Moritz', 'Baring', 6000);
insert into employees values (6, 6, 'Thierry', 'Henry', 5900);
insert into employees values (7, 7, 'Sergio', 'Ramos', 6200);
insert into employees values (8, 8, 'Nikoleta', 'Kyriakopulu', 7000);
insert into employees values (9, 9, 'Aamir', 'Khan', 2000);
insert into employees values (10, 10, 'Takumi', 'Fujiwara', 5000);
insert into employees values (11, 11, 'Heung-min', 'Son', 5100);
insert into employees values (12, 12, 'Peter', 'Johnson', 6100);


SELECT 
emp.first_name, emp.salary, 
cont.anual_adjustment, cont.name,
cty.name,
emp.salary * (1 + cont.anual_adjustment/100) new_salary
FROM employees emp
INNER JOIN countries cty ON cty.id = emp.country_id
INNER JOIN continents cont ON cty.continent_id = cont.id


UPDATE employees
INNER JOIN countries cty ON cty.id = employees.country_id
INNER JOIN continents cont ON cty.continent_id = cont.id
SET salary = salary * (1 + cont.anual_adjustment/100)