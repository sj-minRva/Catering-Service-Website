from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Function to get data from the database
def get_customers():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Catering',
            user='root',
            password='root'
        )
        cursor = connection.cursor(dictionary=True)  # Return data as dictionaries
        cursor.execute("SELECT * FROM customers")  # Fetch all customer data
        customers = cursor.fetchall()
        return customers
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API endpoint to return customer data as JSON
@app.route('/api/customers', methods=['GET'])
def fetch_customers():
    data = get_customers()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
