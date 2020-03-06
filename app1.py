import psycopg2

connection = psycopg2.connect(user = "postgres",
                             password = "",
                             host = "127.0.0.1",
                             port = "",
                             database = "DVRPC") 
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
