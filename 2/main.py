from config import *
import psycopg2
import requests


try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * from orders where createdat >= '2022.06.01' and createdat < '2022.09.01' and statuscode = 'complete' and managerid != 'NULL'"
        )
        
        arr = cursor.fetchall()
        qwerty = {}
        for i in range(90):
            minutes = 0
            quantity = 0
            for j in arr:
                if int(j[4]) == i:
                    minutes += j[3]
                    quantity += 1
            if minutes != 0:
                qwerty[i] = round(minutes / quantity)
        print(qwerty)
        response = requests.post('https://nodus.caseguru.ru/trainee/tasks', json={"task": 2, "result": "4988"})
        print(response.content)
        
        

                    



        
        
        
        

    
except Exception as _ex:
    print("[INFO] Error while working with postgres", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] postgres connect close")





    

        




