import psycopg2

connection = psycopg2.connect(user = "postgres",
                             password = "jinja99",
                             host = "127.0.0.1",
                             port = "5432",
                             database = "DVRPC") 
print("Database successfully opened")

cursor = connection.cursor()

#SQL command to Get count by RECORDNUM 

cursor.execute('''SELECT recordnum, COUNT(recordnum) FROM public.weathersummaries2018 GROUP BY recordnum ORDER BY recordnum ASC;''')

sql_command1 = cursor.fetchall()

for answer1 in sql_command1:
    print(answer1)

print('\n')

#Get all counts sorted by oldest SETDATE to newest - only from bicycleCount2018
    
cursor.execute('''SELECT setdate, COUNT(recordnum1), recordnum1 FROM public.bicyclecount2018 GROUP BY recordnum1 ORDER BY setdate ASC;''')

sql_command2 = cursor.fetchall()

for answer2 in sql_command2:
    print(answer2)

print('\n')

#Get counts filtered by facility type - only be from bicycleCount2018 you have to have add each facility type by using regular expressions, maybe have it appear as a table.

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 GROUP BY bikepedfac;''')
                  
sql_command3 = cursor.fetchall()

for answer3 in sql_command3:
    print(answer3)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE 'Bike Lane%' GROUP BY bikepedfac LIMIT 1;''')
                  
sql_command4 = cursor.fetchall()

for answer4 in sql_command4:
    print(answer4)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Bike Lane%' GROUP BY bikepedfac LIMIT 1;''')
                  
sql_command5 = cursor.fetchall()

for answer5 in sql_command5:
    print(answer5)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sharrow%' GROUP BY bikepedfac LIMIT 1;''')

sql_command6 = cursor.fetchall()

for answer6 in sql_command6:
    print(answer6)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Multiuse Trail%' GROUP BY bikepedfac LIMIT 1;''')

sql_command7 = cursor.fetchall()

for answer7 in sql_command7:
    print(answer7)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Striped Shoulder%' GROUP BY bikepedfac LIMIT 1;''')

sql_command8 = cursor.fetchall()

for answer8 in sql_command8:
    print(answer8)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%N/A%' GROUP BY bikepedfac LIMIT 1;''')

sql_command9 = cursor.fetchall()

for answer9 in sql_command9:
    print(answer9)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sidepath%' GROUP BY bikepedfac LIMIT 1;''')

sql_command10 = cursor.fetchall()

for answer10 in sql_command10:
    print(answer10)

print('\n')

cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Mixed Traffic%' GROUP BY bikepedfac LIMIT 1;''')

sql_command11 = cursor.fetchall()

for answer11 in sql_command11:
    print(answer11)

print('\n')

#Get counts filter by PRCP > 0 Join on SETDATE so I need to do an inner join bicycleCount and weathersummaries using SETDATE and join right/left date of weather summaries where PRCP > 0 

cursor.execute('''SELECT prcp, recordnum1, recordnum FROM public.weathersummaries2018 LEFT JOIN public.bicyclecount2018 ON recordnum = recordnum1 WHERE prcp > 0 ORDER BY setdate;''')

sql_command12 = cursor.fetchall()

for answer12 in sql_command12:
    print(answer12)

print('\n')


#Get 5 counts nearest to a lat/lng position

cursor.execute('''SELECT bikepedfac, sqrt((latitude-75.1652)*(latitude-75.1652) + (longitude-39.9526)*(longitude-39.9526)) as distance, mun_name FROM public.bicyclecount2018 ORDER BY distance LIMIT 5;''')

sql_command13 = cursor.fetchall()

for answer13 in sql_command13:
    print(answer13)

print('\n')

cursor.execute('''SELECT bikepedfac, sqrt((latitude-75.1652)*(latitude-75.1652) + (longitude-39.9526)*(longitude-39.9526)) as distance, mun_name FROM public.bicyclecount2018 ORDER BY bikepedfac LIMIT 5;''')

sql_command14 = cursor.fetchall()

for answer14 in sql_command14:
    print(answer14)

print('\n')

# Get a list of all facility types

#Insert new count

#cursor.execute('''INSERT INTO public.weathersummaries2018 (recordnum, prcp, tavg, tmax, tmin) VALUES (368, 0.500, 24, 60, 17);''')

#connection.commit()
#print("Table info created")

cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 368;''')

sql_command15 = cursor.fetchall()

for answer15 in sql_command15:
    print(answer15)

print('\n')

#Update count by Recordnum

#cursor.execute('''UPDATE public.weathersummaries2018 SET recordnum = 369, prcp = .25, tavg = 19, tmax = 31, tmin = 20  WHERE recordnum = 368;''')

#connection.commit()
#print("Table info updated at recordnum 368, now its 369")

#cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 369;''')

#sql_command16 = cursor.fetchall()

#for answer16 in sql_command16:
#    print(answer16)

#print('\n')

#Delete count by Recordnum

#cursor.execute('''DELETE FROM public.weathersummaries2018 WHERE recordnum = 369;''')

#connection.commit()
#print("Table info deleted at recordnum 369, its been removed")

cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 369;''')

sql_command16 = cursor.fetchall()

for answer16 in sql_command16:
    print(answer16)

connection.close()
print("PostgreSQL connection is closed")


