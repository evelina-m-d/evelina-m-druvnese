DROP TABLE IF EXISTS kafejnicas;
DROP TABLE IF EXISTS darbinieki;
DROP TABLE IF EXISTS pasutijumi;

CREATE TABLE IF NOT EXISTS kafejnicas(
    kafe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    adrese TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS darbinieki(
    darb_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    telefons TEXT NOT NULL,
    amats TEXT NOT NULL,
    darbavieta_id INTEGER NOT NULL,
    atvalinajums BOOLEAN NOT NULL,

    FOREIGN KEY(darbavieta_id) REFERENCES kafejnicas(kafe_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pasutijumi(
    pasutijuma_id INTEGER PRIMARY KEY AUTOINCREMENT,
    summa FLOAT NOT NULL,
    datums DATE NOT NULL,
    apraksts TEXT NOT NULL,
    pasut_darb_id INTEGER NOT NULL,

    FOREIGN KEY(pasut_darb_id) REFERENCES darbinieki(darb_id) ON DELETE CASCADE
);

INSERT INTO kafejnicas (nosaukums, adrese) VALUES
('Pie Jāņa', 'Brīvības iela 10'),
('Zelta Tase', 'Lāčplēša iela 22'),
('Kafijas Stūrītis', 'Valdemāra iela 15'),
('Siltie Rīti', 'Kr. Barona iela 5'),
('Rīta Prieks', 'Elizabetes iela 30');

INSERT INTO darbinieki (vards, uzvards, telefons, amats, darbavieta_id, atvalinajums) VALUES
('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 1, 1),
('Anna', 'Kalniņa', '+37121234567', 'barista', 1, 0),
('Pēteris', 'Ozols', '+37122334455', 'viesmīlis', 2, 0),
('Laura', 'Liepa', '+37121112222', 'vadītāja', 3, 0),
('Mārtiņš', 'Vilks', '+37123456789', 'viesmīlis', 4, 1);

INSERT INTO pasutijumi (summa, datums, apraksts, pasut_darb_id) VALUES
(249.99, '2024-04-01', 'Produkti atvēršanai', 1),
(89.50, '2024-04-03', 'Kafijas pupiņas', 2),
(120.00, '2024-04-04', 'Krūzītes un šķīvji', 3),
(310.40, '2024-04-05', 'Virtuves piederumi', 4),
(99.99, '2024-04-06', 'Deserti', 2),
(45.00, '2024-04-07', 'Papīra maisiņi', 5);

--2.1
SELECT * FROM darbinieki WHERE atvalinajums IS NOT FALSE;

--2.2
SELECT
    COUNT(*) AS "Veikto pasūtījumu skaits"
FROM pasutijumi;

--2.3
SELECT
    darbinieki.vards || ' ' || darbinieki.uzvards AS "Darbinieka vārds",
    COUNT(pasutijumi.pasutijuma_id) AS "Veiktie pasūtījumi"
FROM pasutijumi
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id
GROUP BY darbinieki.darb_id;

--2.4
SELECT
    darbinieki.vards || ' ' || darbinieki.uzvards AS "Darbinieka vārds",
    MAX(pasutijumi.summa) AS "Darbinieka dārgākais pasūtījums"
FROM pasutijumi
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id
GROUP BY darbinieki.darb_id;

--2.5
SELECT
    kafejnicas.nosaukums AS "Kafejnīca",
    ROUND(AVG(pasutijumi.summa), 2) AS "Vidējā pasūtījumu summa"
FROM pasutijumi
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id
LEFT JOIN kafejnicas ON darbinieki.darbavieta_id = kafejnicas.kafe_id
GROUP BY kafejnicas.kafe_id;

--2.6
SELECT
    darbinieki.vards || ' ' || darbinieki.uzvards AS "Darbinieki, kas strādā kā viesmīļi"
FROM darbinieki WHERE amats = "viesmīlis";

--2.7
SELECT * FROM pasutijumi WHERE summa >= 100;

--2.8
SELECT
    kafejnicas.nosaukums AS "Kafejnīca",
    COUNT(pasutijumi.pasutijuma_id) AS "Pasūtījumu skaits" 
FROM pasutijumi
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id
LEFT JOIN kafejnicas ON darbinieki.darbavieta_id = kafejnicas.kafe_id
GROUP BY kafejnicas.nosaukums
ORDER BY "Pasūtījumu skaits" DESC;

--2.9
SELECT
    darbinieki.vards || ' ' || darbinieki.uzvards AS "Darbinieka vārds",
    SUM(pasutijumi.summa) AS "Pasūtījumu summa"
FROM pasutijumi
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id
GROUP BY darbinieki.darb_id;

--2.10
SELECT
    darbinieki.vards || ' ' || darbinieki.uzvards AS "Darbinieka vārds",
    COUNT(pasutijumi.pasutijuma_id) AS "Pasūtījumu skaits"
FROM pasutijumi 
LEFT JOIN darbinieki ON darbinieki.darb_id = pasutijumi.pasut_darb_id 
GROUP BY darbinieki.darb_id
HAVING "Pasūtījumu skaits" >= 2;