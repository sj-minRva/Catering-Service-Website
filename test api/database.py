import mysql.connector
from mysql.connector import Error

def insert_customer(name, email, phone):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='jamesson',
            user='root',
            password='root'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"""
            record = (name, email, phone)
            cursor.execute(insert_query, record)
            connection.commit()
            print("Customer data inserted successfully")
        
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    
    except Error as e:
        print("Error while connecting to MySQL", e)

    

    

    

    

