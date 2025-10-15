--parādīt visus nomniekus
SELECT*FROM nomnieks;

--parādīt visus produktus
SELECT*FROM produkts;

--parādīt tikai nomnieku vārdus un uzvārdus
SELECT vards, uzvards FROM nomnieks;

--parādīt visus produktus, kuru cena ir lielāka par 15 eiro
SELECT nomas_cena_diena,nosaukums FROM produkts WHERE nomas_cena_diena>15;

--parādīt pieejamos produktus (pieejamiba="Jā")
SELECT*FROM produkts where pieejams="Jā";

--atrast visus produktus, ko īrē nomnieks ar id 3
SELECT*FROM noma WHERE nomnieka_id="3";

SELECT*FROM produkts JOIN noma 
ON produkts.produkta_id=noma.produkta_id
WHERE noma.nomnieka_id = "3";


--parādīt visus nomas darījumus ar nomnieka un produkta info
SELECT noma.nomas_objekta_id,nomnieks.vards, nomnieks.uzvards,produkts.nosaukums, noma.sakuma_datums,noma.beigu_datums FROM noma
JOIN nomnieks ON noma.nomnieka_id=nomnieks.nomnieka_id 
JOIN produkts ON noma.produkta_id=produkts.produkta_id;