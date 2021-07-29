# Unit 3 - Sprint 2 Review

## Premise

You are the new Database Architect of a startup family medicine practice that has been keeping records in the most archaic of databases... a ledger!

Your first task is to generate a SQLite database with the ledger provided in the markdown.

Afterwards, your final task will be to query a previously-generated database for some answers to questions.

## Code: Part I

Make a new python script called `health.py`

In your script, create a connection to an empty SQLite3 database called `health_records.sqlite3`

Next, create a table called `patients` with the following columns and datatypes:

1. `patient_id`: integer
2. `patient_name`: text
3. `patient_age`: integer


Now, use the ledger given to you by the receptionist to add the patient's records into the database.

```
 ─────────────────────────────────────────────────
│ *Patient ID* │  *Patient Name*  │ *Patient Age* │
 ─────────────────────────────────────────────────
│       0      │   Rochelle Joy   │      62       │
 ─────────────────────────────────────────────────
│       1      │   Daniel Krieg   │      22       │
 ─────────────────────────────────────────────────
│       2      │   Jamie Klein    │      41       │
 ─────────────────────────────────────────────────
│       3      │   Sam Tillman    │      20       │
 ─────────────────────────────────────────────────
│       4      │   Amanda Bynes   │      30       │
 ─────────────────────────────────────────────────
```

Lastly, perform the following queries on your database - answers will be below the query.

1. `num_patients` - How many patients are there?
   - `>>> [(5,)]`
   
2. `num_patients_over_30` - How many patients are _at least_ 30 years old?
   - `>>> [(3,)]`
   
3. `avg_patient_age` - What is the average patient age?
   - `>>> [(35.0,)]`

## Code: Part II

Create a new python file called `sql.py`

You have a database called `health_db.sqlite3` which contains three tables:

1. `patients`

    - "patient_id": integer
    - "name": text
    - "gender": text ('M'/'F')
    

2. `patient_ailment`

    - "patient_id": integer
    - "patient_ailment": text
    

3. `ailments`

    - "disease": text (same as "patient_ailment")
    - "symptoms": text ('stringified' list of symptoms)
    

Your task is to perform the following queries on the database:

1. `query_total_n_patients` - How many total patients are there?
2. `query_jaundice_symptoms` - What are the symptoms of Jaundice?
3. `query_difference_male_female` - How many more males are there than females? (Only using SQL)
4. `query_most_frequent_ailment` - What is the most frequent patient ailment in the database and its count?
   
For the final query you will need to use a join (either implicit or explicit):

5. `query_names_with_diabetes` - What are the names of all the individuals who have diabetes?

Make sure to write the queries in your `sql.py` script and print out the values.  If it helps, write the queries in
Datagrip first and then copy/paste to the python script.

## Congratulations!

If you felt like this review went well, you should be in a good spot to complete your Sprint Challenge!