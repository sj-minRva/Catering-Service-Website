from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to insert customer data into the database
def insert_customer(name, email, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Catering',
            user='root',
            password='root'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"""
            record = (name, email, password)
            cursor.execute(insert_query, record)
            connection.commit()
            print("Customer data inserted successfully")
        
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    
    except Error as e:
        print("Error while connecting to MySQL", e)

# API to handle customer registration
@app.route('/api/customers', methods=['POST'])
def create_customer():
    customer_data = request.json
    print('Received customer data:', customer_data)

    insert_customer(customer_data['name'], customer_data['email'], customer_data['password'])

    return jsonify({'message': 'Customer data received successfully', 'data': customer_data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
