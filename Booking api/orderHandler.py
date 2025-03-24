from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    try:
        # Get data from the frontend
        data = request.json
        booking_id = data.get("id")  # Extract Booking ID
        items = data.get("items", [])  # Extract items

        if not booking_id or not items:
            return jsonify({"error": "Booking ID and items are required"}), 400

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Save each item with the Booking ID into the database
        for item in items:
            cursor.execute(
                "INSERT INTO orders (bookingID, item_name, quantity) VALUES (%s, %s, %s)",
                (booking_id, item["name"], item["quantity"])
            )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Order placed successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5003)  # Run backend on port 5003
