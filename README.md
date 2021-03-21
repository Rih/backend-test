### Backend Test: Desafío Envíame

El siguiente desafío, busca conocer más respecto a tus habilidades técnicas para abordar y solucionar diferentes problemas. El desafío consta de 7 etapas, las cuales, evaluaremos de manera independiente.

**Asegurate de dejar tu trabajo en un repositorio de github y al finalizar tu tarea nos compartes el repositorio donde deben incluirse todas las instrucciones para que podamos ejecutar tu trabajo de manera local.**

#### Importante: ####
**Los lenguajes a utilizar pueden ser: php, python, node.js**

En caso de preguntas dirigete a: *tech-test@enviame.io*, usando el asunto [Backend-Test]

### Ejercicio 1: Docker

Configura un ambiente en docker que permita ejecutar un entorno web con el stack a tu elección. 
El contenedor de la base de datos debe ser diferente al que contenga tu aplicación, ej: Contenedor 1: Nginx, Contenedor 2: Mysql (composición de servicios docker)

R: 
#### Prerequisitos: 
1. [docker](https://docs.docker.com/get-docker/) 19.03.2 o superior
2. [docker-compose](https://docs.docker.com/compose/install/) 1.24.1 o superior

#### Pasos de instalación
* Ejecutar lo siguiente para construir servidores:
    1. `docker-compose build` o bien `sh bin/build-servers.sh` 
    2. Para iniciar: `docker-compose up -d` o bien `sh bin/start-dev-server.sh`
* Ejecutar lo siguiente para configurar nginx:
    1. `docker exec -it $(docker-compose ps -q web) bash`  o bien `sh bin/enter-web-server.sh`    
    2. Apuntar sitio de nginx para reverse-proxy a uwsgi: `ln -s /nginx/app_back /etc/nginx/sites-enabled/app_back`
    3. Salir: `exit`
    4. cp backend/enviame/local_settings.py.example backend/enviame/local_settings.py
    5. Indicar credenciales de .env en variable DATABASES = {...} de local_settings.py
    6. Reiniciar contenedores:
        - `docker-compose stop` y `docker-compose up -d` o bien `sh/reload-containers.sh`
    7. Si el servidor nginx esta OK: visitar localhost, debiera dar 404 Not Found con una lista urls
    8. Si la BD esta conectada, Ejecutar las migraciones:
        - `docker exec  -it app_web_enviame python3.7 manage.py migrate` o bien `sh bin/migrate.sh`   
    9. Crear assets admin: `docker exec  -it app_web_enviame python3.7 manage.py collectstatic` o bien `sh bin/make-assets.sh`
    10. Crear primer usuario admin: `sh bin/load-init-user.sh` o bien `docker exec  -it app_web_enviame python3.7 manage.py loaddata usuario.json`
    11 Si los assets estan OK: visitar localhost/admin y entrar con el primer usuario
### Ejercicio 2: API REST + CRUD

Dentro del ambiente dockerizado desarrolla una API Rest, con el stack de tu preferencia, que implemente un CRUD de una entidad tipo 'empresa'. Preocupate de incluir un script que genere N registros con datos "fake" (utilizando una librería faker).
* En primer lugar los endpoint estan protegidos por API key
* Debe "iniciar sesion" desde postman para solicitar el access key
    * URL: `http://localhost/api/token/`
    * payload:
    ```json
    {
	    "email": "root@admin.cl",
        "password": "<your_admin_password>"
    }
    ```
  
  * El usuario de ejemplo puede ser creado por el siguiente script si no se hizo en el paso previo:
    * `sh bin/load-init-user.sh` o bien `docker exec  -it app_web_enviame python3.7 manage.py loaddata usuario.json`
    * La contraseña se proporcinará por e-mail a la entrega de este test
    
  * Resultado esperado:
    ```json
      {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjUxMzg0OSwianRpIjoiN2Y3MjIwNTMwNTUxNDY1Yjg1Y2M0MTIwZDliY2E2ODQiLCJ1c2VyX2lkIjoxfQ.SAQmz1hmx8KjIyJKZ4WRHnBXou3sF5pSPCxiUgQvXT4",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MzY5ODQ5LCJqdGkiOiIyYjg0ZTJmNGYwY2M0MzY2OTE5OWQxNTI5Njk1M2E4ZCIsInVzZXJfaWQiOjF9.9EA35dfNaijXns0X8Pa5LhamDjezpDdEEZDVrZfwOvs"
    }
   ```
  * Usar el valor de access en Authorization Bearer $access
  
* Hay un endpoint para generar datos fake de empresa:
    * URL: `http://localhost/api/v1/faker/create-companies/`
    * Header: 
    `Authorization Bearer eyJ0eXA.....LQ-VT_dHis` (access de ejemplo)
    * payload: 
    ```json
    {
      "batch_number": 10
    }
    ```
   


* Hay dos maneras de generar
localhost/api/v1/faker/create-companies/

### Ejercicio 3: Análisis + Desarrollo 

Crea un script en el lenguaje de tu elección y encuentre la(s) cadena de texto que es(son) igual al revés en el siguiente texto:

`afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood`


R: Para ejecutar scripts python puede usar 2 vías: por el ambiente web creado del ejercicio 1 o por virtualenv en la maquina host.
* Opción 1:
    * Levantar contenedor `sh bin/start-dev-server.sh`
    * Ejecutar `sh bin/exercise-3.sh` o bien `docker exec  -it app_web_enviame python3.7 ejercicio_3/palindrome.py`
* Opción 2:
    * Prerequisitos:
        - python3
        - pip
    * Instalar virtualenv: pip install virtualenv
    * Crear un ambiente: 
        - `virtualenv --python='python3' env_iame`
    * Ingresar al ambiente:
        - `source env_iame/bin/activate`  
    * Si aparece en el prompt de la consola (env_viame). Ejecutar:
        - `python backend/ejercicio_3/palindrome.py`   
   
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


R: Para ejecutar scripts python puede usar 2 vías: por el ambiente web creado del ejercicio 1 o por virtualenv en la maquina host.
* Opción 1:
    * Levantar contenedor `sh bin/start-dev-server.sh`
    * Ejecutar `sh bin/exercise-5.sh` o bien `docker exec  -it app_web_enviame python3.7 ejercicio_5/fibo_divisors.py`
* Opción 2:
    * Prerequisitos:
        - python3
        - pip
    * Instalar virtualenv: pip install virtualenv
    * Crear un ambiente: 
        - `virtualenv --python='python3' env_iame`
    * Ingresar al ambiente:
        - `source env_iame/bin/activate`  
    * Si aparece en el prompt de la consola (env_viame). Ejecutar:
        - `python backend/ejercicio_5/fibo_divisors.py` 

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


R: Para ejecutar scripts python puede usar 2 vías: por el ambiente web creado del ejercicio 1 o por virtualenv en la maquina host.
* Opción 1:
    * Levantar contenedor `sh bin/start-dev-server.sh`
    * Ejecutar `sh bin/exercise-6.sh` o bien `docker exec  -it app_web_enviame python3.7 ejercicio_6/estimate_distance.py`
* Opción 2:
    * Prerequisitos:
        - python3
        - pip
    * Instalar virtualenv: pip install virtualenv
    * Crear un ambiente: 
        - `virtualenv --python='python3' env_iame`
    * Ingresar al ambiente:
        - `source env_iame/bin/activate`  
    * Si aparece en el prompt de la consola (env_viame). Ejecutar:
        - `python backend/ejercicio_6/estimate_distance.py` 

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
