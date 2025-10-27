--a)
SELECT * FROM gramatas;

--b)
SELECT nosaukums AS "Grāmatas nosaukums", izdosanas_gads AS "Izdošanas gads" FROM gramatas;

--c)
SELECT * FROM autori;

--d)
SELECT vards AS "Autora vārds", dzimsanas_gads AS "Dzimšanas gads" FROM autori;

--e)
SELECT * FROM zanri;

--f)
SELECT * FROM izdeveji;

--g)
SELECT * FROM gramatas WHERE izdosanas_gads > 1959;

--h)
SELECT * FROM autori WHERE dzimsanas_gads > 1950;

--i)
SELECT * FROM gramatas
ORDER BY izdosanas_gads ASC;

--j)
SELECT * FROM gramatas WHERE zanrs_id = 1;

--k)
SELECT 
    nosaukums AS "Grāmatas nosaukums",
    vards AS "Autora vārds"
FROM gramatas
JOIN autori ON gramatas.autors_id = autori.autors_id
ORDER BY gramatas.nosaukums ASC;

--l)
SELECT 
    nosaukums AS "Grāmatas nosaukums",
    vards AS "Autora vārds",
    izdevejs_nosaukums AS "Grāmatas izdevējs"
FROM gramatas
LEFT JOIN autori ON gramatas.autors_id = autori.autors_id
LEFT JOIN izdeveji ON gramatas.izdevejs_id = izdeveji.izdevejs_id;

--m)
SELECT
    vards AS "Autora vārds",
    COUNT(gramatas.gramatas_id) AS "Autora sarakstīto grāmatu skaits"
FROM gramatas
LEFT JOIN autori ON autori.autors_id = gramatas.autors_id
GROUP BY autori.vards;

--n)
SELECT 
    vards AS "Autora vārds",
    autori.valsts AS "Autora dzimšanas valsts"
FROM autori
JOIN gramatas
ON gramatas.autors_id = autori.autors_id AND gramatas.zanrs_id = 2
GROUP BY autori.autors_id;

--o)
SELECT nosaukums AS "Grāmatas nosaukums", izdosanas_gads AS "Izdošanas gads" FROM gramatas
WHERE izdosanas_gads IN ((SELECT MAX (izdosanas_gads) FROM gramatas), (SELECT MIN (izdosanas_gads) FROM gramatas));