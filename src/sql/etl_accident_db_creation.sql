-- DROP DATABASE IF EXISTS etl_accident;

-- CREATE DATABASE etl_accident;


CREATE TABLE Department
(
    id                  VARCHAR(3) UNIQUE PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

-- CREATE TABLE Town
-- (
--     id                  INT PRIMARY KEY NOT NULL,
--     dept                INT NOT NULL,
--     name                VARCHAR(100),
--
--     FOREIGN KEY (dept)          REFERENCES Department(id)
-- );



CREATE TABLE LumCondition
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE Accident
(
    num_acc             BIGINT PRIMARY KEY NOT NULL,
--     weather_cond        INT,
--     user_type           INT,
    lum                 INT,
--     veh_type            INT,
--     location            INT,
    year                INT,
--     user_number         INT,

--     FOREIGN KEY (weather_cond)    REFERENCES WeatherCondition(id),
--     FOREIGN KEY (user_type)       REFERENCES UserType(id),
    FOREIGN KEY (lum)             REFERENCES LumCondition(id)
--     FOREIGN KEY (veh_type)        REFERENCES VehicleType(id),
--     FOREIGN KEY (location)        REFERENCES Location(id)
);
CREATE TABLE Location
(
    id                  SERIAL PRIMARY KEY NOT NULL,
    dept                VARCHAR(3),
    long                INT,
    lat                 INT,
    num_acc             BIGINT,

    FOREIGN KEY (dept)            REFERENCES Department(id),
    FOREIGN KEY (num_acc)         REFERENCES Accident(num_acc)
);

CREATE TABLE Surface
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE AtmosphericCondition
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE WeatherCondition
(
    id                  SERIAL PRIMARY KEY NOT NULL,
    surface             INT,
    atm                 INT,
    num_acc             BIGINT,

    FOREIGN KEY (surface)         REFERENCES Surface(id),
    FOREIGN KEY (atm)             REFERENCES AtmosphericCondition(id),
    FOREIGN KEY (num_acc)         REFERENCES Accident(num_acc)
--     UNIQUE (surface, atm)
);

-- Categories :
-- 1 – Conducteur
-- 2 – Passager
-- 3 – Piéton
CREATE TABLE UserCategory
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE Gravity
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE UserType
(
    id                  SERIAL PRIMARY KEY NOT NULL,
    place               INT,
    gravity             INT,
    sex                 INT,
    birth_year          INT,
    user_category       INT,
    num_acc             BIGINT,

    FOREIGN KEY (gravity)         REFERENCES Gravity(id),
    FOREIGN KEY (user_category)   REFERENCES UserCategory(id),
    FOREIGN KEY (num_acc)         REFERENCES Accident(num_acc)
);

CREATE TABLE VehicleType
(
    id                  INT PRIMARY KEY NOT NULL,
    name                VARCHAR(100)
);

CREATE TABLE Accident_VehType
(
    num_acc             BIGINT,
    codeVehType         INT,

    FOREIGN KEY (num_acc) REFERENCES Accident(num_acc),
    FOREIGN KEY (codeVehType) REFERENCES VehicleType(id)
--     UNIQUE (num_acc, codeVehType)
);

INSERT INTO VehicleType (id, name) VALUES
    (00, 'Indéterminable'),
    (01, 'Bicyclette'),
    (02, 'Cyclomoteur <50cm3'),
    (03,'Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")'),
    (04, 'Référence inutilisée depuis 2006 (scooter immatriculé)'),
    (05, 'Référence inutilisée depuis 2006 (motocyclette)'),
    (06, 'Référence inutilisée depuis 2006 (side-car)'),
    (07, 'VL seul'),
    (08, 'Référence inutilisée depuis 2006 (VL + caravane)'),
    (09, 'Référence inutilisée depuis 2006 (VL + remorque)'),
    (10, 'VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)'),
    (11, 'Référence inutilisée depuis 2006 (VU (10) + caravane)'),
    (12, 'Référence inutilisée depuis 2006 (VU (10) + remorque)'),
    (13, 'PL seul 3,5T <PTCA <= 7,5T'),
    (14, 'PL seul > 7,5T'),
    (15, 'PL > 3,5T + remorque'),
    (16, 'Tracteur routier seul'),
    (17, 'Tracteur routier + semi-remorque'),
    (18, 'Référence inutilisée depuis 2006 (transport en commun)'),
    (19, 'Référence inutilisée depuis 2006 (tramway)'),
    (20, 'Engin spécial'),
    (21, 'Tracteur agricole'),
    (30, 'Scooter < 50 cm3'),
    (31, 'Motocyclette > 50 cm3 et <= 125 cm3'),
    (32, 'Scooter > 50 cm3 et <= 125 cm3'),
    (33, 'Motocyclette > 125 cm3'),
    (34, 'Scooter > 125 cm3'),
    (35, 'Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)'),
    (36, 'Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)'),
    (37, 'Autobus'),
    (38, 'Autocar'),
    (39, 'Train'),
    (40, 'Tramway'),
    (41, '3RM <= 50 cm3'),
    (42,'3RM > 50 cm3 <= 125 cm3'),
    (43,'3RM > 125 cm3'),
    (50,'EDP à moteur'),
    (60,'EDP sans moteur'),
    (80,'VAE'),
    (99,'Autre véhicule');


INSERT INTO UserCategory (id, name) VALUES
    (0, 'Indeterminé'),
    (1, 'Conducteur' ),
    (2, 'Passager'),
    (3, 'Piéton');

INSERT INTO Gravity (id, name) VALUES
    (0, 'Indeterminé'),
    (1, 'Indemne'),
    (2, 'Tué'),
    (3, 'Blessé hospitalisé'),
    (4, 'Blessé léger');

INSERT INTO LumCondition (id, name) VALUES
    (0, 'Indeterminé'),
    (1, 'Plein jour'),
    (2, 'Crépuscule ou aube'),
    (3, 'Nuit sans éclairage public'),
    (4, 'Nuit avec éclairage public non allumé'),
    (5, 'Nuit avec éclairage public allumé');

INSERT INTO Surface (id, name) VALUES
    (-1, 'Non renseigné'),
    (1, 'Normale'),
    (2, 'Mouillée'),
    (3, 'Flaques'),
    (4, 'Inondée'),
    (5, 'Enneigée'),
    (6, 'Boue'),
    (7 , 'Verglacée'),
    (8, 'Corps gras – huile'),
    (9, 'Autre');

INSERT INTO AtmosphericCondition (id, name) VALUES
    (-1, 'Non renseigné'),
    (1, 'Normale'),
    (2 , 'Pluie légère'),
    (3, 'Pluie forte'),
    (4, 'Neige - grêle'),
    (5, 'Brouillard - fumée'),
    (6, 'Vent fort - tempête'),
    (7, 'Temps éblouissant'),
    (8, 'Temps couvert'),
    (9, 'Autre');