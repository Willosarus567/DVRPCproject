import psycopg2

connection = psycopg2.connect(user = "postgres",
                             password = "",
                             host = "127.0.0.1",
                             port = "",
                             database = "DVRPC") 
print("Database successfully opened") 

cursor = connection.cursor()

cursor.execute('''ALTER TABLE public.bicyclecount2018 ADD FOREIGN KEY (PRCP) REFERENCES public.weathersummaries2018(PRCP);''')

connection.commit()
connection.close()
print("PostgreSQL connection is closed")
