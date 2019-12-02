import psycopg2
from flask import Flask, render_template, url_for, flash, redirect, request, abort

app = Flask(__name__)

connection = psycopg2.connect(user = "postgres",
                             password = "jinja99",
                             host = "127.0.0.1",
                             port = "5432",
                             database = "DVRPC") 
print("Database successfully opened")

cursor = connection.cursor()

@app.route("/DVRPC/")
def DVRPC():
    #SQL command to Get count by RECORDNUM 

    cursor.execute('''SELECT recordnum, COUNT(recordnum) FROM public.weathersummaries2018 GROUP BY recordnum ORDER BY recordnum ASC;''')     
    sql_command1 = cursor.fetchall()
         
    #Get all counts sorted by oldest SETDATE to newest - only from bicycleCount2018
    
    cursor.execute('''SELECT setdate, COUNT(recordnum1), recordnum1 FROM public.bicyclecount2018 GROUP BY recordnum1 ORDER BY setdate ASC;''')
    sql_command2 = cursor.fetchall()
    
    #Get counts filtered by facility type
     
    cursor.execute('''SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE 'Bike Lane%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Bike Lane%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sharrow%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Multiuse Trail%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Striped Shoulder%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%N/A%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sidepath%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac, COUNT(bikepedfac) FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Mixed Traffic%' GROUP BY bikepedfac;''')
                      
    sql_command3 = cursor.fetchall()
    
    
    
    # Get a list of all facility types
    
    cursor.execute('''SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE 'Bike Lane%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Bike Lane%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sharrow%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Multiuse Trail%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Striped Shoulder%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%N/A%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Sidepath%' GROUP BY bikepedfac
                   UNION SELECT bikepedfac FROM public.bicyclecount2018 WHERE bikepedfac LIKE '%Mixed Traffic%' GROUP BY bikepedfac;''')
                      
    sql_command6 = cursor.fetchall()
    
    #Get counts filter by PRCP > 0 Join on SETDATE
    
    cursor.execute('''SELECT prcp, recordnum1, recordnum FROM public.weathersummaries2018 LEFT JOIN public.bicyclecount2018 ON recordnum = recordnum1 WHERE prcp > 0 ORDER BY setdate;''')

    sql_command7 = cursor.fetchall()
    
    
    #Get 5 counts nearest to a lat/lng position
    
    cursor.execute('''SELECT bikepedfac, sqrt((latitude-75.1652)*(latitude-75.1652) + (longitude-39.9526)*(longitude-39.9526)) as distance, mun_name FROM public.bicyclecount2018 ORDER BY distance LIMIT 5;''')

    sql_command8 = cursor.fetchall()
    
    #Insert new count

    cursor.execute('''INSERT INTO public.weathersummaries2018 (recordnum, prcp, tavg, tmax, tmin) VALUES (368, 0.500, 24, 60, 17);''')
    
    connection.commit()
    print("Table info created")
    
    cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 368;''')
    
    sql_command9 = cursor.fetchall()
    
    
    #Update count by Recordnum
    
    cursor.execute('''UPDATE public.weathersummaries2018 SET recordnum = 369, prcp = .25, tavg = 19, tmax = 31, tmin = 20  WHERE recordnum = 368;''')
    
    connection.commit()
    print("Table info updated at recordnum 368, now its 369")
    
    cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 369;''')
    
    sql_command10 = cursor.fetchall()
    
    #Delete count by Recordnum
    
    cursor.execute('''DELETE FROM public.weathersummaries2018 WHERE recordnum = 369;''')
    
    connection.commit()
    print("Table info deleted at recordnum 369, its been removed")
    
    cursor.execute('''SELECT * FROM public.weathersummaries2018 WHERE recordnum = 369 OR recordnum = 361;''')
    
    sql_command11 = cursor.fetchall()
    
    
    return render_template('DVRPC.html', title='DVRPC', route='true', data1 = sql_command1, data2 = sql_command2, data3 = sql_command3, data6 = sql_command6, data7 = sql_command7, data8 = sql_command8, data9 = sql_command9, data10 = sql_command10, data11 = sql_command11)


@app.route("/default/")
def default():
    return render_template('default.html', route='true')

@app.route("/")
def home():
    return render_template('layout.html', title='Home')
    




if __name__ == "__main__":
    app.run()
