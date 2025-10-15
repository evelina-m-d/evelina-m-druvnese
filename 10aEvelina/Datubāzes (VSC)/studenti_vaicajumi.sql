DROP TABLE IF EXISTS atzimes;
DROP TABLE IF EXISTS studentu_kursi;
DROP TABLE IF EXISTS kursi;
DROP TABLE IF EXISTS studenti;

--studenti- glabāt studento info
CREATE TABLE IF NOT EXISTS studenti(
    students_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    epasts NOT NULL UNIQUE CHECK(epasts LIKE '%@%')
);

CREATE TABLE IF NOT EXISTS kursi(
    kurss_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL UNIQUE,
    apraksts TEXT DEFAULT 'Nav apraksta'
);

CREATE TABLE IF NOT EXISTS studentu_kursi(
    sk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_id INTEGER NOT NULL, --norāde uz tabulu studenti
    kurss_id INTEGER NOT NULL, --norāde uz tabulu kursi
    UNIQUE(students_id, kurss_id), --viens students nevar būt divreiz pierakstīts tajā pašā kursā

    FOREIGN KEY(students_id) REFERENCES studenti(students_id) ON DELETE CASCADE, --ja izdzēš studentu vai kursu, tad attiecīgos pierakstus dzēš automātiksi
    FOREIGN KEY(kurss_id) REFERENCES kursi(kurss_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS atzimes(
    atzimes_id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_id INTEGER NOT NULL,
    kurss_id INTEGER NOT NULL,
    atzime INTEGER NOT NULL CHECK(atzime BETWEEN 1 AND 10),

    FOREIGN KEY(students_id) REFERENCES studenti(students_id) ON DELETE CASCADE, --ja izdzēš studentu vai kursu, tad attiecīgos pierakstus dzēš automātiksi
    FOREIGN KEY(kurss_id) REFERENCES kursi(kurss_id) ON DELETE CASCADE
    --kombinacija studenta id un kursa id nevar atkartoties
    UNIQUE (students_id, kurss_id)
);

--studentu pievienošana

INSERT INTO studenti(vards,uzvards,epasts) VALUES
    ('Anna', 'Bēržiņa', 'annab@gmail.com'),
    ('Jānis', 'Kalniņš', 'jkalnins@gmail.com'),
    ('Jana', 'Mīļā', 'jm@gmail.com'),
    ('Rinda', 'Māja', 'rindumajas@gmail.com'),
    ('Alnis', 'Kaija', 'zoodarzs@gmail.com');

INSERT INTO kursi(nosaukums,apraksts) VALUES
    ('Mongoļu kakla dziedāšana', 'Apgūsiet seno mongoļu mākslu no mongoļu pasniedzēja. Tikai mongoļu valodā'),
    ('Matemātika II', 'Dzirdēsiet vairāk par skolotāja dzīvi nekā par matemātiku'),
    ('Angļu valodas literatūra', 'Skolotājs runā tik monotoni, ka aizmigsiet'),
    ('Deguna urbināšana II', 'Pasniedzējai ir doktora grāds nekā nedarīšanā, tāpēc viņa ļoti atbilst šim kursam pat tad, ja grāds nav tajā pašā jomā');

INSERT OR IGNORE INTO studentu_kursi(students_id, kurss_id) VALUES
    (1,2), (1,4), --Anna
    (2,1), (2,3), -- Jānis
    (3,1), (3,2), --Jana
    (4,4), --Rinda
    (5,4), (5,3); --Alnis

INSERT INTO atzimes (students_id, kurss_id, atzime) VALUES
    (1,2,9), (1,4,10), --Anna
    (2,1,4), (2,3,7), --Jānis
    (3,1,3), (3,2,7), --Jana
    (4,4,10), --Rinda
    (5,4,9), (5,3,5); --Alnis

--visus studentus parādīt dilstošā secībā pēc uzvārdiem
SELECT * FROM studenti ORDER BY uzvards DESC;

--paradit visus kursus un studentus, kas tajos pierakstiti
SELECT
    kursi.nosaukums AS kursa_nosaukums, --parskatamibai maina kolonnas nosaukumu
    studenti.vards || ' ' || studenti.uzvards AS students --apvieno vardu ar uzvardu
FROM kursi
JOIN studentu_kursi ON kursi.kurss_id = studentu_kursi.kurss_id
JOIN studenti ON studentu_kursi.students_id = studenti.students_id
ORDER BY kursi.nosaukums;

--saskaitit cik studentu ir katra kursa
SELECT
    kursi.nosaukums AS Kursa_nosaukums,
    COUNT(studentu_kursi.students_id) AS Studentu_skaits
FROM kursi
LEFT JOIN studentu_kursi ON kursi.kurss_id = studentu_kursi.kurss_id
GROUP BY kursi.nosaukums;
