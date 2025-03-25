from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Function to establish a database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Catering"
    )

# API Endpoint: Fetch and merge bookings and orders
@app.route('/merged-data', methods=['GET'])
def get_merged_data():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT 
                b.id AS booking_id,
                b.name,
                b.contact,
                b.event_date,`
                b.guests,
                b.food_type,
                COALESCE(GROUP_CONCAT(o.item_name SEPARATOR ', '), 'No Orders') AS items,
                COALESCE(GROUP_CONCAT(o.quantity SEPARATOR ', '), 'No Orders') AS quantities
            FROM bookings b
            LEFT JOIN orders o ON b.id = o.bookingID
            GROUP BY b.id;
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(data)

    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {str(err)}"}), 500

# Run the server on port 5007
if __name__ == '__main__':
    app.run(debug=True, port=5007)
