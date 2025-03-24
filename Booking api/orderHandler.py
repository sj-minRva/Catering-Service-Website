from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "Catering"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root")
    )

# API to save orders
@app.route("/api/orders", methods=["POST"])

def save_order():
    connection = None
    cursor = None
    try:
        data = request.json  # Get JSON data from frontend
        items = data.get("items", [])  # Extract order items

        if not items:
            return jsonify({"error": "No items provided"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert each item into the database
        for item in items:
            cursor.execute("INSERT INTO orders (item_name, quantity) VALUES (%s, %s)",
                           (item["name"], item["quantity"]))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Order placed successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5003)  # Running on port 5003