from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Fetch Customers from Database
def get_customers():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'Catering'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'root')
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bookings")
        customers = cursor.fetchall()
        return customers
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return {"error": str(err)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API Endpoint to Fetch Data
@app.route('/api/customers', methods=['GET'])
def fetch_customers():
    data = get_customers()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Running on port 5000
