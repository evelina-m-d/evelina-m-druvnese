DROP TABLE IF EXISTS televizijas_sovi;
DROP TABLE IF EXISTS sovu_dalibnieki;
DROP TABLE IF EXISTS sovu_dalibas;

CREATE TABLE IF NOT EXISTS televizijas_sovi(
    sova_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    kanals TEXT NOT NULL,
    zanrs TEXT NOT NULL,
    gads INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sovu_dalibnieki(
    dalibnieka_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    profesija TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sovu_dalibas(
    dalibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sovu_dalibnieki_id INTEGER NOT NULL,
    televizijas_sovi_id INTEGER NOT NULL,
    loma TEXT NOT NULL,

    FOREIGN KEY(sovu_dalibnieki_id) REFERENCES sovu_dalibnieki(dalibnieka_id) ON DELETE CASCADE,
    FOREIGN KEY(televizijas_sovi_id) REFERENCES televizijas_sovi(sova_id) ON DELETE CASCADE
);

INSERT INTO televizijas_sovi (nosaukums, kanals, zanrs, gads) VALUES
('X Faktors', 'TV3', 'Mūzika', 2017),
('Balss maskā', 'TV3', 'Mūzika', 2020),
('Supernova', 'LTV1', 'Konkurss', 2015),
('Lauku sēta', 'Go3', 'Sarunu šovs', 2011),
('Gudrs, vēl gudrāks', 'LTV1', 'Spēle', 2012);



INSERT INTO sovu_dalibnieki (vards, uzvards, profesija) VALUES
('Aija', 'Ozoliņa', 'Žurnāliste'),
('Jānis', 'Kalniņš', 'Šefpavārs'),
('Elīna', 'Bērziņa', 'Režisore'),
('Roberts', 'Liepiņš', 'Ārsts'),
('Laura', 'Mežs', 'Profesors'),
('Mārtiņš', 'Krastiņš', 'Šefpavārs'),
('Baiba', 'Grīnberga', 'Pasākumu vadītāja'),
('Kristaps', 'Ozols', 'Ārsts'),
('Rūta', 'Ābele', 'Grima māksliniece'),
('Gatis', 'Vilsons', 'Ārsts'),
('Dace', 'Eglīte', 'Redaktore'),
('Renārs', 'Ziediņš', 'Profesors');


INSERT INTO sovu_dalibas (sovu_dalibnieki_id, televizijas_sovi_id, loma) VALUES
(1, 1, 'Dalībniece'),
(1, 3, 'Dalībniece'),
(2, 1, 'Dalībnieks'),
(2, 4, 'Dalībnieks'),
(3, 2, 'Vadītāja'),
(3, 5, 'Vadītāja'),
(4, 1, 'Dalībnieks'),
(4, 3, 'Dalībnieks'),
(5, 2, 'Dalībniece'),
(6, 4, 'Dalībnieks'),
(7, 5, 'Vadītāja'),
(8, 4, 'Dalībnieks'),
(9, 1, 'Dalībniece'),
(9, 5, 'Dalībniece'),
(10, 3, 'Dalībnieks'),
(11, 3, 'Žūrija'),
(12, 3, 'Žūrija'),
(12, 1, 'Viesis');

--a)
SELECT 
    nosaukums AS "Nosaukums",
    kanals AS "Kanāls",
    zanrs AS "Žanrs"
FROM televizijas_sovi;

--b)
SELECT
    vards AS "Vārds",
    uzvards AS "Uzvārds",
    profesija AS "Profesija"
FROM sovu_dalibnieki WHERE profesija = 'Ārsts'; 

--c)
SELECT
    nosaukums AS "Nosaukums",
    kanals AS "Kanāls",
    gads AS "Gads"
FROM televizijas_sovi WHERE gads > 2018;

--d)
SELECT
    nosaukums AS "Nosaukums",
    kanals AS "Kanāls"
FROM televizijas_sovi WHERE kanals = 'TV3' OR kanals = 'Go3';

--e)
SELECT
    sovu_dalibnieki.vards || ' ' || sovu_dalibnieki.uzvards AS "Dalībnieka vārds",
    televizijas_sovi.nosaukums AS "Šova nosaukums",
    sovu_dalibas.loma AS "Dalībnieka loma šovā"
FROM sovu_dalibas
LEFT JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.dalibnieka_id
LEFT JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.sova_id
GROUP BY sovu_dalibas.dalibas_id
ORDER BY televizijas_sovi.nosaukums DESC;

--f)
SELECT
    televizijas_sovi.nosaukums AS "Šova nosaukums",
    sovu_dalibnieki.vards || ' ' || sovu_dalibnieki.uzvards AS "Žūrijas vārds"
FROM sovu_dalibas 
LEFT JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.dalibnieka_id
LEFT JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.sova_id
WHERE sovu_dalibas.loma = 'Žūrija'
GROUP BY sovu_dalibas.dalibas_id;

--g)
SELECT
    kanals AS "Kanāls",
    COUNT(nosaukums) AS "Šovu skaits šajā kanālā"
FROM televizijas_sovi
GROUP BY kanals
ORDER BY "Šovu skaits šajā kanālā" ASC;

--h)
SELECT
    sovu_dalibnieki.vards || ' ' || sovu_dalibnieki.uzvards AS "Dalībnieka vārds",
    COUNT(televizijas_sovi.sova_id) AS "Dalībnieka šovu skaits"
FROM sovu_dalibas
LEFT JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.dalibnieka_id
LEFT JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.sova_id
GROUP BY sovu_dalibnieki.dalibnieka_id
ORDER BY "Dalībnieka šovu skaits" ASC;

--i)
SELECT
    televizijas_sovi.nosaukums AS "Šova nosaukums",
    COUNT(sovu_dalibnieki.dalibnieka_id) AS "Dalībnieku skaits šovā"
FROM sovu_dalibas
LEFT JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.dalibnieka_id
LEFT JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.sova_id
GROUP BY televizijas_sovi.nosaukums;

--j)
SELECT
    sovu_dalibnieki.vards || ' ' || sovu_dalibnieki.uzvards AS "Dalībnieka vārds",
    COUNT(televizijas_sovi.sova_id) AS "Dalībnieka šovu skaits"
FROM sovu_dalibas
LEFT JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.dalibnieka_id
LEFT JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.sova_id
GROUP BY sovu_dalibnieki.dalibnieka_id
HAVING "Dalībnieka šovu skaits" > 1;