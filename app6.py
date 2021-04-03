import psycopg2

connection = psycopg2.connect(user = "",
                             password = "",
                             host = "",
                             port = "",
                             database = "") 
print("Database successfully opened") 

cursor = connection.cursor()

cursor.execute('''ALTER TABLE public.bicyclecount2018 ADD FOREIGN KEY (PRCP) REFERENCES public.weathersummaries2018(PRCP);''')

connection.commit()
connection.close()
print("PostgreSQL connection is closed")
