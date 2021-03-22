-- SCRIPT DDL CHANGED TO PostgreSQL version

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

insert into continents values (1, 'América', 4);
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
