import sqlite3


conn = sqlite3.connect('health_records.sqlite3')
curs = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER,
    patient_name TEXT,
    patient_age INTEGER
);
"""

curs.execute(create_table)

patient_insert = """
INSERT INTO patients VALUES
    (0, 'Rochelle Joy', 62),
    (1, 'Daniel Krieg', 22),
    (2, 'Jamie Klein', 41),
    (3, 'Sam Tillman', 20),
    (4, 'Amanda Bynes', 30);
"""

curs.execute(patient_insert)

conn.commit()

# QUERIES
num_patients = """
SELECT COUNT(*)
FROM patients;
"""

num_patients_over_30 = """
SELECT COUNT(*)
FROM patients
WHERE patient_age >= 30;
"""

avg_patient_age = """SELECT AVG(patient_age) FROM patients;"""

queries = [num_patients, num_patients_over_30, avg_patient_age]

for query in queries:
    results = curs.execute(query).fetchall()
    print(results)

conn.close()
