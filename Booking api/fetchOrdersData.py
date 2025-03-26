from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to fetch orders from the database
def get_orders():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "Catering"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root")
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        return orders
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return {"error": str(err)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API Endpoint to Fetch Data
@app.route('/api/orders', methods=['GET'])
def fetch_orders():
    print("Fetching orders from the database...")
    data = get_orders()
    if isinstance(data, dict) and "error" in data:
        print("Error fetching orders:", data["error"])
        return jsonify({"error": data["error"]}), 500
    else:
        print(f"Successfully fetched {len(data)} orders.")
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5004)  # Run backend on port 5004
