import psycopg2

connection = psycopg2.connect(user = "postgres",
                             password = "jinja99",
                             host = "127.0.0.1",
                             port = "5432",
                             database = "DVRPC") 
print("Database successfully opened") 

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE bicyclecount2018
               (RECORDNUM1 INT REFERENCES public.weathersummaries2018(RECORDNUM),
                SETDATE DATE, 
                LATITUDE NUMERIC(4, 2),
                LONGITUDE NUMERIC(4, 2),
                CO_NAME CHAR(100),
                MUN_NAME CHAR(100),
                BIKEPEDFAC CHAR(100),
                PRIMARY KEY(RECORDNUM1));''')

connection.commit()
connection.close()
print("PostgreSQL connection is closed")
