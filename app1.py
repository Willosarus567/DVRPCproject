import psycopg2

connection = psycopg2.connect(user = "",
                             password = "",
                             host = "",
                             port = "",
                             database = "") 
print("Database successfully opened") 

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE weathersummaries2018
               (RECORDNUM INT NOT NULL,
                PRCP NUMERIC(26,13),
                TAVG INT,
                TMAX INT,
                TMIN INT,
                PRIMARY KEY(RECORDNUM));''')

connection.commit()
connection.close()
print("PostgreSQL connection is closed")
